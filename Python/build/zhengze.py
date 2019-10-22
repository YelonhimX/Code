import requests
import re
from bs4 import BeautifulSoup
import bs4

def getHTML(url):
    '''
    需要注意的是，淘宝页面爬取需要登录cookies
    以下12行到16行就是编辑cookies的过程
    '''
    kv = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    usercookies = "t=684edbb0ad3447a0b8309bde706ee296; cna=xWPyFVosrVcCAW8oxZC1M8XM; thw=cn; lgc=tb13289283; tracknick=tb13289283; tg=0; mt=ci=0_1; enc=GN0eYRLiSZPf1YYgGyb8Ggz3VzkPmCaiS%2FFLixhxJ%2BMZ8XOES758bNgiDgPK5iURfflbWCxng9xGCeAMKhGmBg%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; cookie2=743b5aebbebb887827b23da274a82893; _tb_token_=9ba5e6b78753; unb=3365090684; uc3=id2=UNN79Hu46I5xQA%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&nk2=F5REPQPr65EmWw%3D%3D&vt3=F8dByuHZ7kjZ2ravrg4%3D; csg=d34362a0; cookie17=UNN79Hu46I5xQA%3D%3D; dnk=tb13289283; skt=bb5f94bd37fe92dc; existShop=MTU2OTY5MzUyMQ%3D%3D; uc4=id4=0%40UgQz1yN%2FASfQtG9PoxEcMkmAUfGB&nk4=0%40FY4Pb2hzCHoyQ4FwG2dj1LPTn%2BuX; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=34b; _nk_=tb13289283; cookie1=BxUMWqCyesrnB24sCMMgaPAcJDMobZCxwzk2nipIoB4%3D; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTaEcfFG6o%2BXQ%3D%3D&tag=8&lng=zh_CN; isg=BJmZudLmIId4X_zwzCi5TqgmqIVzJo3Ymatt-LtOIEA5wrlUA3adqAfQwIa0-iUQ; l=cBSbiUkPqHNT9TbyBOCanurza77OSIRYYuPzaNbMi_5aw6Tsi6QOk6DxIF96VjWd9NTB4tm2-gv9-etkZ8--WOHgcGAN."
    #审查元素——搜索sw.js

    #cookie的处理部分

    cookies = {}
    #服务器要求cookies是字典类型
    #以下是处理cookies文本
    for a in usercookies.split(';'):#以“；”作为划分切割文本
        name,value=a.strip().split('=',1)#split方法可以将等号两遍的字符分割，strip方法可以去除字符串中多余的空格
        cookies[name]=value
    try:
        r = requests.get(url,cookies=cookies,headers=kv,timeout = 30)#request.get方法可以允许携带头文件和cookie访问
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return False

def editData(plist,html):
    try:
        prt = re.findall(r'"view_price":"\d*\.\d{2}"',html)#正则表达式
        nmt = re.findall(r'"raw_title":".*?"',html)
        for i in range(len(prt)):
            prize = prt[i].split(':')[1].strip("\" ")
            itname = nmt[i].split(':')[1].strip("\"")
            plist.append([prize,itname])       
    except:
        return False
def printOut(plist):
    tplt = '{:8}\t{:16}\t'
    print(tplt.format("价格","商品名"))
    for j in plist:
        print(tplt.format(j[0],j[1]))
        
def main():
    turl = "https://s.taobao.com/search?q="
    item = input("请输入你想搜索的物品：")
    depth = input("请输入你想搜索的深度：")
    depth = int(depth)
    cnt = []
    for i in range(depth):
        try: 
            url = turl + item + "&s=" + str(44*i)
            html = getHTML(url)
            editData(cnt,html)
        except:
            continue
    printOut(cnt)

main()
