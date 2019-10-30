# -*- coding: utf-8 -*-
import scrapy
from marxspider.items import MarxspiderItem

class MarxSpider(scrapy.Spider):
    name = 'marx'
    allowed_domains = ['marxists.org']
    start_urls = ['https://marxists.org/chinese/marx-engels/01/index.htm']

    def parse(self, response):
        item = MarxspiderItem()
        item["link"] = response.xpath("//a[@href]").extract()
        
            
        yield item
       