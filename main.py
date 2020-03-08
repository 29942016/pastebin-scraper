from pymongo import MongoClient
from dbAccessors import CanReachDatabase
from bs4 import BeautifulSoup
import os
import requests

# os.system('cls')
# soup.find(id='id_name')
# soup.find_all('section', class_='class_name')


def main():
    if CanReachDatabase() == False:
        exit

    print('==============')
    url = 'https://pastebin.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    lUrlsContainer = soup.find(id='menu_2')
    lAnchorTags = lUrlsContainer.find_all('a')

    for anchorTag in lAnchorTags:
        print(anchorTag.attrs['href'], ' - ', anchorTag.contents[0])

  #  print(lPastes.prettify())

    print('====\nEND')


main()
