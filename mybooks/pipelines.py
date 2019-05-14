# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class MybooksPipeline(object):

    # 爬虫开始前执行一次（初始化工作）
    def open_spider(self, spider):
        # self.f = open("books.txt", "a", encoding="utf-8")
        # 连接MongoDB数据库服务器
        self.db_client = pymongo.MongoClient()
        # 指定操作数据库的对象
        self.db = self.db_client["scrape"]
        # 指定集合（类似MYSQL中的表)
        self.db_collection = self.db["books"]

    def process_item(self, item, spider):
        # 处理数据
        # with open("books.txt","a",encoding="utf-8")as f:
        # book_str = item["name"] + ";" + item["price"] + "\n"
        # self.f.write(book_str)
        # return item
        self.db_collection.insert_one(dict(item))
        return item

    # 爬虫全部完成后执行一次（收尾工作）
    def close_spider(self, spider):
        # self.f.close()
        self.db_client.close()
