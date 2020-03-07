from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#获取页面中所有内链的列表
def getInternalLinks(bs,includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,
        urlparse(includeUrl).netloc)
    internaLinks = []
    #找出所有以“/”开头的链接
    for link in bs.find_all('a',
                            href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internaLinks:
                if (link.attrs['href'].startwith('/')):
                    internaLinks.append(
                        includeUrl+link.attrs['href'])
                else:
                    internaLinks.append(link.attrs['href'])
    return internaLinks

#获取页面中所有外链的列表
def getExternalLinks(bs,excludeUrl):
    excludeLinks = []
    #找到所有以“http”或“www”开头且不包含当前URL的链接
    for link in bs.find_all('a',
                            href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in excludeLinks:
                excludeLinks.append(link.attrs['href'])
    return excludeLinks

def getRandomExternalLink(startingpage):
    html = urlopen(startingpage)
    bs = BeautifulSoup(html,'lxml')
    externalLinks = getExternalLinks(bs,
                                     urlparse(startingpage).netloc)
    if len(externalLinks) == 0:
        print('No external links,looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingpage).scheme,
                                  urlparse(startingpage).netloc)
        internalLinks = getInternalLinks(bs,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is : {}'.format(externalLink))
    followExternalOnly(externalLink)

followExternalOnly('http://ent.zdface.com/mxkb/2020-01-14/862968_3.shtml')