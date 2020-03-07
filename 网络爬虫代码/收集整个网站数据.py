from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,lxml

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html,'lxml')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mv-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span')
              .find('a').attrs['href'])
    except AttributeError as e:
        print('页面缺少了一些属性！不过不用担心！')

    for link in bs.find_all('a',href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇到了新的页面
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks(' ')
