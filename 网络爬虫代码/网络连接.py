from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import lxml

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError:
        print('Http Error.')
    except URLError:
        print('The server could not be found!')
    else:
        try:
            bs = BeautifulSoup(html.read(),'lxml')
            title = bs.body.h1
        except AttributeError as e:
            print('Attribute Error')
        else:
            if title == None:
                print('Title could not be found.')
            else:
                print(title.get_text())

title = getTitle('https://www.apple.com.cn/cn/ipad/compare/')