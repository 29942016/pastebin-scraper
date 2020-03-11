from pymongo import MongoClient
from dbAccessors import CanReachDatabase
from scraper import GetTenUrls
import time
import os

# os.system('cls')
# soup.find(id='id_name')
# soup.find_all('section', class_='class_name')

test = 'asdf'


def main():
    if CanReachDatabase() == False:
        exit

    while 1 == 1:
        GetTenUrls()
        print('Sleeping...')
        time.sleep(30)


main()
