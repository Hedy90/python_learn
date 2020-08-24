#子标签(.children)与后代标签(.descendants)的关系:子标签就是一个父标签的下一级，而后代标签是指一个父标签下面所有级别的标签。所有的子标签都是后代标签，但不是所有的后代标签都是子标签。
#兄弟标签：next_siblings、previous_siblings
#父标签：parent

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

url="http://www.pythonscraping.com/pages/page3.html"
html=get_html(url)
soup=analyze_html(html)
for child in soup.find('table',{'id':'giftList'}).children: #通过.children生成器,可以对指定标签（此处为table标签）的子标签进行遍历
    print(child)
print(len(list(soup.table.children))) #打印上述子标签的个数，结果为13

print('分隔符')

for child in soup.find('table',{'id':'giftList'}).descendants: #通过.descendants生成器,可以对指定标签（此处为table标签）的后代标签进行遍历
    print(child)
print(len(list(soup.table.descendants))) #打印上述子标签的个数，结果为86

print(len(list(soup.children))) #打印该HTML文档的所有子标签个数，结果为2
print(len(list(soup.descendants))) #打印该HTML文档的所有后代标签个数，结果为122

for sibling in soup.find('table',{'id':'giftList'}).tr.next_siblings: #next_siblings,兄弟标签，可用于收集表格数据。不包含第一行的表格标题。理由有二：对象不能把自己作为兄弟标签。任何时候获取一个标签的兄弟标签，都不会包含这个标签本身。其次，这个函数只调用后面的兄弟标签。例如，如果我们选择一组标签中位于中间位置的一个标签，然后用next_siblings()函数，那么它就只会返回在它后面的兄弟标签。因此，选择标签行然后调用next_siblings，可以选择表格中除了标题行以外的所有行。
    print(sibling)

print(soup.find('img',{'src':'../img/gifts/img2.jpg'}).parent.previous_sibling.get_text())
#此处的父标签执行流程如下：
#定位到img标签中src属性为../img/gifts/img2.jpg的标签
#定位到img标签的父标签（此处为<td>标签）
#定位到该父标签<td>的前一个兄弟标签previous_sibling（此处为包含美元价格的<td>标签）
#打印标签中的文字信息：$10,000.52