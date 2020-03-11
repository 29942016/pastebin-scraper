from pymongo import MongoClient
from dto.scrape import Scrape
from pymongo.errors import ServerSelectionTimeoutError


def GetClient():
    dbName = 'data'
    collectionName = 'scrapes'
    client = MongoClient('localhost', 27017)
    db = GetDbCollection(client, dbName)
    return db


def CanReachDatabase():
    dbName = 'data'
    collectionName = 'scrapes'
    client = MongoClient('localhost', 27017)

    db = GetDbCollection(client, dbName)

    if db == False:
        return False

    table = DoesTableExist(db, collectionName)

    if table == False:
        return False

    data = table.find({})
    total = table.estimated_document_count()

    print('[DB] ', dbName, '->', collectionName)
    print('[DB] Total Entries: ', total)
    print('=====================\n')

    for document in data:
        temp = Scrape(document['_id'], document['user'], document['misc'])
        print(temp)

    return True


def GetDbCollection(client, dbName):
    if DoesDatabaseExist(client, dbName):
        return client[dbName]
    else:
        print('[ERR] Failed to find database.')
        return False


def DoesDatabaseExist(client, dbName):
    try:
        dbNames = client.list_database_names()
        if dbName in dbNames:
            return True
        else:
            return False
    except ServerSelectionTimeoutError:
        print('[ERR] Server Timeout.')
        return False


def DoesTableExist(dbObject, collectionToFind):
    tables = dbObject.collection_names()
    if collectionToFind in tables:
        return dbObject[collectionToFind]
    else:
        print('[ERR] Failed to find table.')
        return False


def InsertDocument(table, url, hit, content):
    client = GetClient()

    if(client):
        newDocument = {"url": url, "hit":  hit, "content": content}
        client[table].insert_one(newDocument)
