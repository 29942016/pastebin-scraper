import os
from pymongo import MongoClient
from accessors import CanReachDatabase


def main():
    os.system('cls')

    if CanReachDatabase() == False:
        exit


main()
