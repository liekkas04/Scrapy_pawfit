import scrapy
import os
from tutorial.items import TutorialItem, PawfitItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["pawfit.com"]
    start_urls = [
        "https://www.pawfit.com/",
        'https://www.pawfit.com/product.html',
        'https://www.pawfit.com/how-it-works.html'
    ]

    def parse(self, response):
        item=PawfitItem()
        item['url']=response.url
        item['body']="测试数据"
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        return item

if __name__ == '__main__':
    # os.system('scrapy genspider pawfit www.pawfit.com')
    os.system("scrapy crawl dmoz")