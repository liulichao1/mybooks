# @Time : 2019/5/14 10:04
# @Author : 2273360936@qq.com
# @FileName : books_spider.py
# @GitHub : https://github.com/liulichao1/mybooks
from scrapy.spiders import Spider  # 爬虫模块
from scrapy import Request  # 请求模块
from mybooks.items import MybooksItem
import re


class booksSpider(Spider):
    name = "books"  # 爬虫的名称
    start_urls = ["http://books.toscrape.com/"]

    #  爬虫功能
    def parse(self, response):
        # 数据提取功能
        li_selector = response.xpath("//ol/li")
        for li in li_selector:
            item = MybooksItem()  # 生成了Item类的对象
            name = li.xpath("article/h3/a/text()").extract_first()
            price = li.xpath("article/div[last()]/p[@class='price_color']/text()").extract()[0]
            item["name"] = name
            item["price"] = price
            yield item

        next_url = response.xpath("//li[@class='next']/a/@href").extract()
        if next_url:
            next_url = "http://books.toscrape.com/catalogue/page-" + re.sub("\D", "", next_url[0]) + ".html"
            yield Request(next_url)
