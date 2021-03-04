import scrapy
from scrapy.linkextractors import LinkExtractor
import os

from tutorial.items import PawfitItem
from tutorial.pipelines import PawfitPipeline


class PawfitSpider(scrapy.Spider):
    name = 'pawfit'
    set = set()
    items = PawfitItem()
    allowed_domains = ['www.pawfit.com']
    start_urls = ['https://www.pawfit.com/',
                  'https://www.pawfit.com/product.html',
                  'https://www.pawfit.com/how-it-works.html'
                  ]

    def parse(self, response):
        le = LinkExtractor()
        # file=open('url.txt',mode='w')
        # 过滤规则的启动
        self.items['title']='抓取网站链接'
        self.items['url']=response.url
        print(response.url)
        links = le.extract_links(response)
        yield self.items
        for link in links:
            scrapy.Request(link.url,callback=self.parse)
            urls=le.extract_links(response)
            for url in urls:
                scrapy.Request(url.url, callback=self.parse)
                yield scrapy.Request(url.url, callback=self.parse_item)
    def parse_item(self,response):
        self.items['title'] = '抓取网站链接'
        self.items['url']=response.url
        yield self.items

if __name__ == '__main__':
    os.system('scrapy crawl pawfit')