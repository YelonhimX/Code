# -*- coding: utf-8 -*-
import scrapy


class Demo2Spider(scrapy.Spider):
    name = 'demo2'
    #allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/video/online.html']

    def parse(self, response):
        fname = response.url.split('/')[-1].split('?')[-2]
       
        with open(fname,'wb') as f:
            f.write(response.body)
        
