import csv
import pandas as pd
from pymongo import MongoClient
import ast 

def csv_to_mongodb(csv_file_path, db_name, collection_name, mongo_uri="mongodb://djadmin:DJsuggester2025!@mongodbitk.duckdns.org:27017/"):
    df = pd.read_csv(csv_file_path)
    
    data = df.to_dict(orient='records')
    
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    
    if data:
        result = collection.insert_many(data)
        print(f"Inserted {len(result.inserted_ids)} documents into '{db_name}.{collection_name}'")
    else:
        print("No data found in the CSV file.")
    
    client.close()

def insert_dj_events(csv_file, mongo_uri="mongodb://djadmin:DJsuggester2025!@mongodbitk.duckdns.org:27017/", db_name="DJSuggestionsDB", collection_name="DJEvent"):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    fieldnames = ["ID", "DJID", "QRCode", "MusicConfig"]

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, fieldnames=fieldnames)
        
      
        documents = []
        for row in reader:
            try:
                row["MusicConfig"] = ast.literal_eval(row["MusicConfig"])
            except (SyntaxError, ValueError):
                row["MusicConfig"] = {}
            
        
            
            documents.append(row)

    if documents:
        result = collection.insert_many(documents)
        print(f"Inserted {len(result.inserted_ids)} documents into {db_name}.{collection_name}")
    else:
        print("No records found to insert.")
    
    client.close()

def insert_playlists(csv_file, mongo_uri="mongodb://djadmin:DJsuggester2025!@mongodbitk.duckdns.org:27017/", db_name="DJSuggestionsDB", collection_name="Playlist"):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    fieldnames = ["ID", "UserID", "MusicList"]

    documents = []
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, fieldnames=fieldnames)
       
        for row in reader:
            try:
                row["MusicList"] = ast.literal_eval(row["MusicList"])
            except (SyntaxError, ValueError):
                row["MusicList"] = []

          
            documents.append(row)

    if documents:
        result = collection.insert_many(documents)
        print(f"Inserted {len(result.inserted_ids)} documents into {db_name}.{collection_name}")
    else:
        print("No documents found to insert.")

    client.close()

if __name__ == "__main__":
    CSV_FILE1 = "./dummy-data/DJEvent.csv"
    CSV_FILE2 = "./dummy-data/GuestUser.csv"
    CSV_FILE3 = "./dummy-data/Playlist.csv"
    CSV_FILE4 = "./dummy-data/User.csv"
    DB_NAME = "DJSuggestionsDB"

    
    csv_to_mongodb(CSV_FILE2, DB_NAME, "GuestUser")
    csv_to_mongodb(CSV_FILE4, DB_NAME, "User")
    insert_dj_events(CSV_FILE1)
    insert_playlists(CSV_FILE3)

