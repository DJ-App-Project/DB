from pymongo import MongoClient
import datetime
import time
import os

# Povezava na MongoDB
MONGO_URI = "mongodb://djadmin:DJsuggester2025!@mongodbitk.duckdns.org:27017/"
client = MongoClient(MONGO_URI)

# Izberi bazo
db = client["DJSuggestionsDB"]

# Seznam kolekcij, ki jih spremljamo
collections = ["DJEvent", "GuestUser", "Playlist", "Songs", "User"]

# Funkcija za generiranje unikatnega imena za datoteko
def generate_log_filename():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"audit_logs_{timestamp}.txt"
    return log_filename

# Nastavi ime datoteke
LOG_FILE = generate_log_filename()

# Funkcija za zapis sprememb v datoteko
def log_change(change, collection_name):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"\n[{timestamp}] Collection: {collection_name} | Operation: {change['operation']}\n"

        # Če je bila dodana nova vrstica
        if change["operation"] == "insert":
            log_entry += f"Inserted Document: {change['document']}\n"

        # Če je bila posodobitev, zapišemo samo spremenjena polja
        elif change["operation"] == "update":
            log_entry += f"Updated Fields: {change['updated_fields']}\n"

        # Če je bil dokument izbrisan
        elif change["operation"] == "delete":
            log_entry += f"Deleted Document ID: {change['document_id']}\n"

        file.write(log_entry)
        print(log_entry)  # Tudi izpišemo v terminal

# Funkcija za sledenje spremembam v kolekcijah (polling)
def watch_changes():
    print(f"Polling collections for changes... Logging to: {LOG_FILE}\n")

    # Shranjevanje zadnjih ID-jev, da lahko spremljamo nove spremembe
    last_seen = {coll: None for coll in collections}

    while True:
        for collection_name in collections:
            collection = db[collection_name]

            # Pridobimo zadnji dokument v kolekciji, da bi spremljali spremembe
            last_document = collection.find().sort([('$natural', -1)]).limit(1)

            if last_document:
                last_document = list(last_document)[0]
                last_id = last_document["_id"]
                
                # Če je prišlo do novega dokumenta ali posodobitve
                if last_seen[collection_name] is None or last_seen[collection_name] != last_id:
                    # Logiramo spremembo
                    change = {
                        'operation': 'insert',
                        'document': last_document
                    }
                    log_change(change, collection_name)
                    last_seen[collection_name] = last_id

        # Čakanje nekaj sekund pred ponovnim pregledovanjem
        time.sleep(5)

# Zaženi spremljanje
watch_changes()
