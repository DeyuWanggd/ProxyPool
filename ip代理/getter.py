from db import db
from crawl_proxies import Crawler
from config import *
class Getter(object):
    def __init__(self):
        self.db = db()
        self.crawler = Crawler()
    def run(self):
        print("获取器开始执行")
        for i in range(self.crawler.__ProxiesCount__):
            callback = self.crawler.__Proxies__[i]
            proxies = self.crawler.get_proxies(callback=callback)
            for proxie in proxies:
                self.db.add_proxie(proxie)


