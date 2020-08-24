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

url="http://www.pythonscraping.com/pages/warandpeace.html"
html=get_html(url)
soup=analyze_html(html)
for name in soup.find_all('span',{'class':'green'}): #遍历HTML文档中span标签下、class值为green的内容，并以文本形式打印。.get_text()函数会把正在处理的HTML文档中所有的标签都清除，然后返回一个只包含文字的字符串。假如正在处理一个包含许多超链接、段落和标签的大段源代码，那么.get_text()会把这些超链接、段落和标签都清除掉，只剩下一串不带标签的文字。
    print(name.get_text())

namelist=soup.find_all(text='the prince') #掌握find、find_all函数的用法，此处表示遍历HTML中的内容，将文本为the prince的内容存入namelist，然后用len函数即可得出文本the prince出现的次数
print(len(namelist))