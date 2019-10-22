import os  # 这里需要额外引入一个os读写库

import requests

url  = "https://cdn.pixabay.com/photo/2019/09/13/14/31/elephant-4474027_960_720.jpg"
root = "D://pics//"
path = root + url.split('/')[-1]#
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url,timeout = 500)
        with open(path,'wb') as f:
            f.write(r.content)
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
