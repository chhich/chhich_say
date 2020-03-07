from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml,re,random,datetime

random.seed(datetime.datetime.now())
def getLinks(url):
   url_wiki = 'https://en.wikipedia.org'
   url_search = url_wiki + url
   html = urlopen(url_search)
   bs = BeautifulSoup(html,'lxml')
   return bs.find('div',{'id':'bodyContent'}).find_all(
            'a',href=re.compile('^(/wiki/)((?!:).)*$'))


links = input('Please input what are you want search in wiki:')
new_links = re.sub(r'\s','_',links)
check = re.compile('^(/wiki/)[^A-Za-z0-9_]')
if check.search(new_links) is not None:
    print('Please input in English!')
else:
    L = getLinks(new_links)


while len(L) > 0:
    newArticle = L[random.randint(0,len(L)-1)].attrs['href']
    print(newArticle)
    L = getLinks(newArticle)