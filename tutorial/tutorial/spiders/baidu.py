# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


# 继承的是CrawlSpider
class DemoSpider(CrawlSpider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com']

    # 定义提取url地址的规则
    rules = (
        # LinkExtractor 链接提取器，提取url地址
        # callback 提取出来的url地址的response会交给callback处理（如果不需要处理，可以不写callback）
        # follow 提取的url地址的响应是否重新经过rules来提取新url地址（默认False）
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item'),  # callback不能传递数据。 详情页的url
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+\.htm'), follow=True),  # 下一页的url
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul",)), callback="parse_item"),
    # 也可以通过XPath匹配对应标签中的所有url
        # 如果url匹配到上面的规则，就不会继续向下匹配了。
    )

    # parse函数有特殊功能，不能定义(覆盖)
    def parse_item(self, response):
        item = {}
        item["title"] = re.findall("<!--TitleStart-->(.*?)<!--TitleEnd-->", response.body.decode())[0]
        item["publish_date"] = re.findall("发布时间：(20\d{2}-\d{2}-\d{2})", response.body.decode())[0]
        print("**************"+item)

    #     也可以继续发送请求(可以通过meta传递数据)
    #     yield scrapy.Request(
    #         url,
    #         callback=self.parse_detail,
    #         meta = {"item":item}
    #     )
    #