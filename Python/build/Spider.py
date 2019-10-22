import requests
r = requests.get("http://www.pornhub.com")#requests 的get函数
print(r.status_code)                        #目前网站的状态，200表示成功
print(r.apparent_encoding)                  #目前网站的编码    
#r.encoding = 'utf-8'
print(r.text)