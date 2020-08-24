# coding=utf-8
 
import requests#导入requests包
from bs4 import BeautifulSoup#从bs4导入beautifulsoup包
 
# 获取html文档的函数，下面会调用
def get_html(url):
    """get the content of the url"""
    response = requests.get(url)#从链接获取所有的网页源码
    response.encoding = 'utf-8'#转化编码模式为utf-8
    return response.text#返回转化之后的源码
    
# 获取笑话的函数，下面会调用
def get_certain_joke(html):
    """get the joke of the html"""
    soup = BeautifulSoup(html, 'lxml')#使用lxml解析器对网页进行解析（可以使用默认解析器，但是lxml解析器功能更加强大）
    joke_content = soup.select('a[class="MsoNormal"]')[0].get_text()#获取标签为a，属性class为"recmd-content"的内容，取第一条的内容（可以查看网页源码之后确定搜索的内容）
    return joke_content#返回得到的内容
 
url_joke = "https://kf.qq.com/faq/140225MveaUz1501077rEfqI.html"#网页地址
html = get_html(url_joke)#获取网页源码
joke_content = get_certain_joke(html)#获取内容
print (joke_content)#打印获取的内容