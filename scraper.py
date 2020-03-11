from bs4 import BeautifulSoup
import requests
import scraper
import os
import re
from dbAccessors import InsertDocument

_url = 'https://pastebin.com'
_raw = _url + '/raw'


def GetTenUrls(skipKeys):
    items = {}
    page = requests.get(scraper._url)
    soup = BeautifulSoup(page.content, 'html.parser')

    lUrlsContainer = soup.find(id='menu_2')
    lAnchorTags = lUrlsContainer.find_all('a')

    for anchorTag in lAnchorTags:
        _url = anchorTag.attrs['href']
        _id = anchorTag.contents[0]
        items[_url] = _id

    for key in items:
        # Don't analyze already analyzed pastes.
        if(key in skipKeys):
            print('skipping ' + key)
            continue

        content = FetchPasteData(key, items[key])
        hits = Analyze(content)

        # insert to db
        if(hits):
            InsertDocument('emails', key, hits, content.decode('utf-8'))

    # Updated what we've analyzed to cache
    return items


def FetchPasteData(url, id):
    page = requests.get(_raw + url)

    if(page.status_code == 404):
        print('Failed to fetch: ', url)
        return False

    return page.content


def Analyze(data):
    html = data.decode('utf-8')
    #pEmail = r'[\w\.-]+@[\w\.-]+'
    pEmail = r'[\w\.-]+@[\w\.-]\.[\w\.-]+'
    results = re.findall(pEmail, html)
    if(results):
        for result in results:
            print(result)
        return results
    else:
        print('no results.')

    print('===')
    return False
