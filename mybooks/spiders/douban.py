# @Time : 2019/5/15 14:15
# @Author : 2273360936@qq.com
# @FileName : douban.py
# @GitHub : https://github.com/liulichao1/mybooks
from scrapy.spiders import Spider
from scrapy import Request
from mybooks.items import MoviesItem
import json


class doubanSpider(Spider):
    name = "douban"

    def start_requests(self):
        url = "https://movie.douban.com/j/search_subjects?type=movie&tag=最新&page_limit=20&page_start=0"
        yield Request(url)

    def parse(self, response):
        movies_dict = json.loads(response.text)  # 字典类型

        for one_movie in movies_dict["subjects"]:
            item = MoviesItem()
            item["title"] = one_movie["title"]
            item["rate"] = one_movie["rate"]
            item["url"] = one_movie["url"]
            item["img"] = one_movie["cover"]
            yield item
