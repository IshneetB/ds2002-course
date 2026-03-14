import os
from pymongo import MongoClient



MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

def main():

    client = MongoClient(
        MONGODB_ATLAS_URL,
        username=MONGODB_ATLAS_USER,
        password=MONGODB_ATLAS_PWD
    )

    db = client["bookstore"]
    authors = db["authors"]

    total = authors.count_documents({})
    print("Bookstore Authors Report")
    print("Total number of authors:", total)
    print()

    for author in authors.find():
        print("Name:", author["name"])
        print("Nationality:", author["nationality"])
        print()

    client.close()

if __name__ == "__main__":
    main()
