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

url="https://www.jianshu.com/p/2b783f7914c6"
html=get_html(url)
soup=analyze_html(html)
for link in soup.find_all('link'):
    print(link.get('href'))