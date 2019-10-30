# -*- coding: utf-8 -*-
import scrapy


class MarxSpider(scrapy.Spider):
    name = 'marx'
    allowed_domains = ['marxists.org']
    start_urls = ['http://marxists.org/']

    def parse(self, response):
        pass
