from pymongo import MongoClient
import datetime

# Povezava na MongoDB
MONGO_URI = "mongodb://djadmin:DJsuggester2025!@mongodbitk.duckdns.org:27017/"
client = MongoClient(MONGO_URI)

# Izberi bazo
db = client["DJSuggestionsDB"]

# Seznam kolekcij, ki jih spremljamo
collections = ["DJEvent", "GuestUser", "Playlist", "Songs", "User"]

# Datoteka za shranjevanje logov
LOG_FILE = "audit_logs.txt"

# Funkcija za zapis sprememb v datoteko
def log_change(change, collection_name):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"\n[{timestamp}] Collection: {collection_name} | Operation: {change['operationType']}\n"

        # Če je bila dodana nova vrstica
        if change["operationType"] == "insert":
            log_entry += f"Inserted Document: {change['fullDocument']}\n"

        # Če je bila posodobitev, zapišemo samo spremenjena polja
        elif change["operationType"] == "update":
            log_entry += f"Updated Fields: {change['updateDescription']['updatedFields']}\n"

        # Če je bil dokument izbrisan
        elif change["operationType"] == "delete":
            log_entry += f"Deleted Document ID: {change['documentKey']}\n"

        file.write(log_entry)
        print(log_entry)  # Tudi izpišemo v terminal

# Spremljanje sprememb v vseh kolekcijah
def watch_changes():
    print("Watching for changes in collections...\n")

    # Ustvarimo Change Stream za vse kolekcije
    pipelines = [db[coll].watch() for coll in collections]

    # Spremljamo vse naenkrat
    for pipeline, coll_name in zip(pipelines, collections):
        def watch_pipeline():
            for change in pipeline:
                log_change(change, coll_name)
        
        from threading import Thread
        Thread(target=watch_pipeline, daemon=True).start()

# Zaženi spremljanje
watch_changes()

# Drži program aktiven (npr. v Dockerju ali strežniku)
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Stopping change stream monitoring.")
