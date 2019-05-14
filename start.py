# @Time : 2019/5/14 11:18
# @Author : 2273360936@qq.com
# @FileName : start.py
# @GitHub : https://github.com/liulichao1/mybooks
from scrapy import cmdline
cmdline.execute("scrapy crawl books -o books.csv".split())