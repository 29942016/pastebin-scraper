from pymongo import MongoClient


def GetDbCollection(client, dbName):
    if DoesDatabaseExist(client, dbName):
        return client[dbName]
    else:
        print('Failed to find database')
        return False


def DoesDatabaseExist(client, dbName):
    dbNames = client.list_database_names()
    if dbName in dbNames:
        return True
    else:
        return False


def DoesTableExist(dbObject, collectionToFind):
    tables = dbObject.collection_names()
    if collectionToFind in tables:
        return dbObject[collectionToFind]
    else:
        return False
