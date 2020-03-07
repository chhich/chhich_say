import requests,lxml
from bs4 import BeautifulSoup

class content:
    '''
    所有文章/网页的共同基类
    '''

    def __init__(self,topic,url,title,body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        '''
        用灵活的打印函数控制结果
        '''
        print("New article found for topic:{}".format(self.topic))
        print("URL:{}".format(self.url))
        print("TITLE:{}".format(self.title))
        print("BODY:\n{}".format(self.body))

class website:
    '''
    描述网站结果的信息
    '''
    def __int__(self,name,url,searchUrl,resultListing,
                resultUrl,absoluteUrl,titleTag,bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler:

    def getPage(self,url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text,'lxml')

    def safeGet(self,pageObj,selector):
        '''
        用于从一个BeautifulSoup对象和一个选择器获取内容的辅助函数。
        如果选择器没有找到对象，就返回空字符串
        '''
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''

    def search(self,topic,site):
        '''
        根据主题搜索网站并记录所有找到的页面
        '''
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs['href']
            #检查一下是相对URL还是绝对URL
            if(site.absolutUrl):
                bs = self.getPage(Url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print('Something was wrong with that page or URL. Skipping!')
                return
            title = self.safeGet(bs,site.titleTag)
            body = self.safeGet(bs,site.bodyTag)
            if title != ' ' and body != ' ':
                content = Content(topic,title,body,url)
                content.print

crawler = Crawler()

...