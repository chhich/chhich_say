import requests
from bs4 import BeautifulSoup

url = 'http://m.qiushi.92game.net/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
links = requests.get(url,headers=headers)
print(links.text)