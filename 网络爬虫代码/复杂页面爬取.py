from urllib.request import urlopen
from bs4 import BeautifulSoup
import attr
import lxml,re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html,'lxml')
# TODO: 提高筛选的精准性，将“//”，“/wiki/”，“#cite_note”等开头的链接删除
for link in bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])