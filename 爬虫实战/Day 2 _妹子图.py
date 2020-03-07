import requests
import lxml
from bs4 import BeautifulSoup

url = 'http://www.mzitu.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'Referer':'http://www.mzitu.com'
    }

Picreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'Referer': 'http://i.mzitu.net'
    }

start_html = requests.get(url,headers=headers)

path = 'E://mzitu'

soup = BeautifulSoup(start_html.text,'html.parser')
page = soup.find_all('a',class_='page-numbers')
max_page = page[-2].text

same_url = 'https://www.mzitu.com/mm/'

for i in range(1,int(max_page) + 1):
    ul = same_url + str(i)

    start_html = requests.get(ul,headers=headers)

    soup = BeautifulSoup(start_html.text,'html.parser')
    all_a = soup.find('div',class_='postlist').find_all('a',target=='_blank')

    for a in all_a:
        title = a.get_text()
        if(title != ''):
            print('准备爬取：' + title)

            if(os.path.exists(path + title.strip().replace('?',''))):
                flag = 1
            else:
                os.makedirs(path + title.strip().replace('?',''))
                flag = 0
            os.chdir(path + title.strip().replace('?',''))

            href = a['href']
            html = requests.get(href,headers=headers)
            mess = BeautifulSoup(html.text,'html.parser')

            pic_max = mess.find_all('span')
            pic_max = pic_max[9].text
            if(flag == 1 and len(os.listdir(path + title.strip().replace('?','')))) >= int(pic_max):
                print('已经保存完毕，跳过。')
                continue

            for num in range(1,int(pic_max) + 1):
                pic = href + '/' + str(num)

                html = requests.get(pic,headers=headers)
                mess = BeautifulSoup(html.text,'html.parser')
                pic_url = mess.find('img',alt=title)
                print(pic_url['src'])
                html = requests.get(pic_url['src'],headers=Picreferer)

                file_name = E:// + pic_url['src'].split('//')[-1]

                f = open(file_name,'wb')
                f.write(html.content)
                f.close()
            print('完毕。')
    print('第',n,'页完毕。')


