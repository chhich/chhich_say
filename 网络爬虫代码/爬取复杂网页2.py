from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,lxml

pages = set()
def getLinks(pageurl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageurl))
    bs = BeautifulSoup(html,'lxml')
    for link in bs.find_all('a',href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                getLinks(newPage)
getLinks(' ')
