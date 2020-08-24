import requests
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

url="https://kf.qq.com/faq/140225MveaUz1501077rEfqI.html"
html=get_html(url)
soup=analyze_html(html)
print(soup.title) #打印title标签（含标签名、标签内容）
print(soup.title.name) #打印title标签的标签名
print(soup.title.string) #打印title标签中的内容
print(soup.title.parent.name) #打印title标签的父标签名称
print(soup.h1) #打印h1标签（含标签名、标签内容）
print(soup.h1.string) #打印h1标签中的内容
print(soup.h1['class']) #打印h1标签内容中class属性的内容
print(soup.div) #打印div标签（含标签名、标签内容），只打印第一个
# print(soup.find_all('div')) #打印所有div标签（含标签名、标签内容）
print(soup.find(id='kf_search_key')) #打印指定ID的内容

# for link in soup.find_all('img'): #找到所有img标签，并打印该标签中的链接
#    print(link.get('src'))

# print(soup.get_text()) #获取html中的所有文字内容

print(soup.body.div) #打印body标签下的第一个div标签（div标签为body的子标签,即子节点）
print(soup.head.contents) #contents可以将tag的子节点以列表的方式输出
print(soup.head.contents[0])