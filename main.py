from pymongo import MongoClient
from dbAccessors import CanReachDatabase
from scraper import GetTenUrls
import os

# os.system('cls')
# soup.find(id='id_name')
# soup.find_all('section', class_='class_name')

test = 'asdf'


def main():
    if CanReachDatabase() == False:
        exit

    pastes = GetTenUrls()


main()
