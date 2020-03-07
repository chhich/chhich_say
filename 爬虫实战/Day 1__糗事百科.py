import requests,lxml
from bs4 import BeautifulSoup

url = 'http://m.qiushi.92game.net/'
def gettexts(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    links = requests.get(url,headers=headers)
    get_con(links)

def get_con(links):
    soup = BeautifulSoup(links,'lxml')
    con_list = soup.find_all('p','class="user"')
    for i in con_list:
        output = '作者：{}，内容：{}，点赞：{}，反对：{}，评论：{}'
        author = i.find('img').get_text()
        con = i.find('class="qiushi"').get_text()
        vote = i.find('a','class="vote"').find('span').string
        down = i.find('a','class="down"').find('span').string
        comment = i.find('a','class="qiushi_comments"').get_text()

        save_con(output.format(author,con,vote,down,comment))

def save_con(*args):
    for i in args:
        with open('c:\\users\\mi\\qiushi','w',encoding='utf-8') as f:
            f.write(i)

gettexts(url)