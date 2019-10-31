#- * -coding: utf - 8 - * -

#Define your item pipelines here## Don 't forget to add your pipeline to the ITEM_PIPELINES setting
#See: https: //docs.scrapy.org/en/latest/topics/item-pipeline.html


class MarxspiderPipeline(object):   
    def process_item(self, item, spider): 
    #for ir in range(item["link"]):
        print(item["link"])
        return item
