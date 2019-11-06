# -*- coding: utf-8 -*-
import scrapy


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['biliblil.com']
    start_urls = ['https://www.bilibili.com/video/av73063155/']

    def parse(self, response):
        root = "fake.html"
        with open(root,'wb') as f:
            f.write(response)
       
            
