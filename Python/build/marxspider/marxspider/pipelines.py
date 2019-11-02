#- * -coding: utf - 8 - * -

#Define your item pipelines here## Don 't forget to add your pipeline to the ITEM_PIPELINES setting
#See: https: //docs.scrapy.org/en/latest/topics/item-pipeline.html


class MarxspiderPipeline(object):   
    def process_item(self, item, spider): 
    #for ir in range(item["link"]):
        fname = 'text.txt'
        with open(fname,'ab') as f:
            #二进制打开
            text = item["text"]
            #.encode('utf-8')←这里的text是list类型.encode方法不合法
            for cnt in text:
                f.write(cnt.encode('utf-8'))
                #遍历list类型里的每一个元素进行写入
        return item
