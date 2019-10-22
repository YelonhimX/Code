import requests
import bs4
from bs4 import BeautifulSoup
import re
'''
模块化编程，编程前先构思程序结构，需要一个爬取数据的函数getHTML()，需要一个将爬取的数据筛选并存放的函数putINList(),
需要一个输出函数printOut()。


'''
def getHTML(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "
       
def putINList(ulist, html):
    soup = BeautifulSoup(html , "html.parser")
    for tr in soup.find('tbody').children:#这里soup.find()函数是搜索Html内容里所有tbody标题下的子标题
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
'''
    for i in soup.find_all(True):
        print(i.name)               #这段是通过soup.find_all函数查找网页源代码中所有标签并输出
'''


def printOut(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"#使用format格式化输出，正则表达式限定格式
    print(tplt.format("排名","学校名称","省市",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))     
def main():

    uinfo = []
    num = input("请输入您想要查看至的大学排名：")
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html =getHTML(url)
    putINList(uinfo,html)
    printOut(uinfo,int(num))
main()
    