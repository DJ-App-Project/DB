import csv
import pandas as pd
from pymongo import MongoClient

def insert_songs(csv_file, mongo_uri="mongodb://djadmin:DJsuggester2025!@mongodbitk.duckdns.org:27017/", db_name="djSuggestions", collection_name="songs"):
    """ Function to insert song data from a CSV file into MongoDB. """
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    df = pd.read_csv(csv_file)

    documents = df.to_dict(orient="records")

    if documents:
        result = collection.insert_many(documents)
        print(f"Inserted {len(result.inserted_ids)} documents into {db_name}.{collection_name}")
    else:
        print("No documents found to insert.")

    client.close()

if __name__ == "__main__":
    CSV_FILE_SONGS = "./dummy data/Songs.csv"
    insert_songs(CSV_FILE_SONGS)
