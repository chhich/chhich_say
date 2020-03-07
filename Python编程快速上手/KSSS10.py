#                           CSS选择器的例子
#传递给 select()方法的选择器                       将匹配
#soup.select('div')                        所有名为<di>的元素
#soup.select('＃author')                   带有id属性为 author的元素
#soup.select('.notice')                    所有使用 CSS class属性名为 notice的元素
#soup.select('div span')                   所有在<div>元素之内的<span>元素
#soup.select('div >span')                  所有直接在<div>元素之内的<span>元素,中间没有其他元素
#soup.select('input[name]')                所有名为<input>,并有一个name属性,其值无所谓的元素
#soup.select('input[type＝"button"]')      所有名为<input>,并有一个type属性, button其值为的元素

#启动selenium控制浏览器
from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com')
#selenium 的 Webdriver方法，用于查找元素
#browser . find_element_by_class_name (name)
#browser . find_elements_by_class_name (name)
#browser . find_elements_by_css_selector ( selector)
#browser . find_element_by_id (id)
#browser . find_elements_by_id ( id )
#browser . find_element_by_link_text ( text)
#browser . find_elements_by_link_text ( text )
#browser . find_element_by_partial_link_text ( text )
#browser.find_elements_by_partial_link_text ( text )
#browser . find_element_by_name ( name )
#browser . find_elements_by_name ( name )
#browser . find_clement_by_tag_name ( name )
#browser . find_elements_by_tag_name ( name )

#点击页面
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
linkElem.click()  # follows the "Read It Online" link

#填写并提交表格
browser = webdriver.Firefox()
browser.get('gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('ichhch.m@gmail.com')
passwordElem = browser.find_element_by_id('passwd')
passwordElem.send_keys('xxxxxx')
passwordElem.submit()

#发送特殊键
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.HOME)
#Keys.(...)

# 项目1：“I'm Feeling Lucky"Google 查找
import requests, webbrowser, sys, bs4
print('Googling...')
res = requests.get('http://google.com/searching?=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

#Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

#项目2: 下载所有XKCD漫画
import requests, os, bs4
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True) #store comics in ./xkcd
while True:
    #Dowload the page.
    print('Downloading the page %s' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    #Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comiv image.')
    else:
        comicUrl = comicElem[0].get('src')
    #Dowload the image.
    print('Downloading image %s' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

    #Save the image to  ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #Get the prev button's url
    prevLink = soup.select('a[rel="prev"]')(0)
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')


import pip._internal
print(pip._internal.