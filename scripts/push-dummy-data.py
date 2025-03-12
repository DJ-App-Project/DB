
import pandas as pd
from pymongo import MongoClient

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

if __name__ == "__main__":
    CSV_FILE1 = "../dummy-data/DJ_Events_Data.csv"
    CSV_FILE2 = "../dummy-data/Guest_Users_Data.csv"
    CSV_FILE3 = "../dummy-data/Music_Config_Data.csv"
    CSV_FILE4 = "../dummy-data/Music_Data.csv"
    CSV_FILE5 = "../dummy-data/Playlists_Data.csv"
    CSV_FILE6 = "../dummy-data/Users_Data.csv"
    DB_NAME = "dj-app-test"

    
    csv_to_mongodb(CSV_FILE1, DB_NAME, "dj-events")
    csv_to_mongodb(CSV_FILE2, DB_NAME, "guest-users")
    csv_to_mongodb(CSV_FILE3, DB_NAME, "music-config")
    csv_to_mongodb(CSV_FILE4, DB_NAME, "music-data")
    csv_to_mongodb(CSV_FILE5, DB_NAME, "playlists-data")
    csv_to_mongodb(CSV_FILE6, DB_NAME, "users-data")
