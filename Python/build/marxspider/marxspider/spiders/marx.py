# -*- coding: utf-8 -*-
import scrapy
from marxspider.items import MarxspiderItem
from scrapy.http import HtmlResponse
from scrapy.selector import Selector

class MarxSpider(scrapy.Spider):
    name = 'marx'
    allowed_domains = ['marxists.org']
    start_urls = ['https://marxists.org/chinese/marx-engels/01/index.htm']

    def parse(self, response):
        url = 'https://marxists.org/chinese/marx-engels/01/'
        item = MarxspiderItem()
        item["link"] = response.xpath("//a/@href").re(r'\d{3}.htm.*?')
        #每个链接的编号，xpath+正则，其实这样麻烦了,scrapy麻烦就在于此，一个for循环就解决的问题。
        for ir in item["link"]:
            urls = url+ir
            #print(urls)
        #print(len(item["link"]))
        #调试用
            yield scrapy.Request(urls,callback=self.text_parse)
            #回调函数，下一步爬取requests
    
    def text_parse(self, response):
        #爬取每一个章节的文字
        item = MarxspiderItem()
        text = response.xpath("//body/text()|/html/body/div[2]/table/tbody/tr/td/text()").extract()
        #通过观察网页源代码得出需要爬取的字符串块
        #注意到response.text返回的是文本型内容
        #而如果想要爬取图片可以采用response.content方法
        item["text"] = text
        yield item

        
