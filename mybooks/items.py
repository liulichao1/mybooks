# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MybooksItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()#  书籍名称
    price = scrapy.Field() #  价格
    url = scrapy.Field()#  链接地址
    content = scrapy.Field()#  书籍简介


class MoviesItem(scrapy.Item):
    title = scrapy.Field()  #
    rate = scrapy.Field()  #
    url = scrapy.Field()  #
    img = scrapy.Field()  #

