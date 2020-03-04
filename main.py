import os
from pymongo import MongoClient
from accessors import DoesDatabaseExist, DoesTableExist, GetDbCollection
from dto.scrape import Scrape


def main():
    os.system('cls')

    dbName = 'data'
    collectionName = 'scrapes'
    client = MongoClient('localhost', 27017)

    db = GetDbCollection(client, dbName)

    if db == False:
        print('Failed to find database:' + dbName)
        exit

    table = DoesTableExist(db, collectionName)

    if table == False:
        print('Failed to find table: ' + collectionName)
        exit

    print('[DB] ', dbName, '->', collectionName)
    print('=====================\n')

    data = table.find({})
    total = table.estimated_document_count()

    print('Total Entries: ', total)
    for document in data:
        temp = Scrape(document['_id'], document['user'], document['misc'])
        print(temp)


main()
