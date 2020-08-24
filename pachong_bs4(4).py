#正则表达式，利用正则表达式抓取图片链接

import requests
import re
from bs4 import BeautifulSoup

#获取HTML文档
def get_html(url):
    try:
        response=requests.get(url)
    except requests.HTTPError as e:
        print(e)
        print("status_code",response.status_code)
        return None
    response.encoding='utf-8'
    return response.text

#解析HTML文档
def analyze_html(html):
    soup=BeautifulSoup(html) #使用默认解析器对HTML进行解析
    return soup

url="http://www.pythonscraping.com/pages/page3.html"
html=get_html(url)
soup=analyze_html(html)

#方法一：通过定位图片链接标签来查找
for link in soup.find_all('img'): #图片的标签是img，遍历所有的img标签，然后打印标签对应的src值
    print(link.get('src'))

print('分隔符')

#方法二：通过正则表达式来查找，这种方法在页面发生变化时仍适用，此种方法更优。正则表达式可以作为bs语句的任意一个参数，让目标原色查找工作几句灵活性。
images=soup.find_all('img',{'src':re.compile("\.\.\/img\/gifts\/img.*\.jpg")}) #正则释义：.*指单个字符匹配任意次，即贪婪匹配
for link2 in images:
    print(link2.get('src'))

# lambda表达式，通过该表达式选择标签，有时是正则表达式的完美替代方案