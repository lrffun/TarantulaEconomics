import scrapy


class EastmoneySpider(scrapy.Spider):
    name = 'eastMoney'
    allowed_domains = ['http://data.eastmoney.com']
    start_urls = ['http://http://data.eastmoney.com/notices']

    def parse(self, response):
        pass
