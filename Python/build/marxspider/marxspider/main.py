from scrapy.cmdline import execute
import sys
import os
# 获取当前脚本路径
dirpath = os.path.dirname(os.path.abspath(__file__))
print(dirpath)
# 添加环境变量
sys.path.append(dirpath)
# 启动爬虫,第三个参数为爬虫name
execute(['scrapy','crawl','marx'])
#————————————————
#版权声明：本文为CSDN博主「这孩子谁懂哈」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/zhaomengszu/article/details/88885852