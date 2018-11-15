import redis
from config import *
import re
import time
from random import choice
class db(object):
    def __init__(self,host = REDIS_HOST,port = REDIS_PORT,password = REDIS_PASSWORD):
        '''连接数据库'''
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)
    def add_proxie(self,proxie,score=FIRST_SOCRE):
        '''添加代理进入数据库,添加的代理还未进行测试,分数为0'''
        ip = re.compile(r"(1?\d?\d.|2[0-4]\d.|25[1-5].){3}(1?\d?\d|2[1-4]\d|25[1-5]):\d+")
        if re.match(ip,proxie[10:]):
            self.db.zadd(REDIS_KEY,score,proxie)
    def del_proxie(self,proxie):
        try:
            self.db.zrem(REDIS_KEY,proxie)
        except:
            pass
    def update_proxie(self,proxie):
        self.db.zadd(REDIS_KEY,time.time(),proxie)
    def get_proxie(self):
        try:
            num = self.count_proxie()
            proxies = self.db.zrange(REDIS_KEY,num-30,num)
            return choice(proxies)
        except:
            print("代理池内没有数据")
    def count_proxie(self):
        return self.db.zcard(REDIS_KEY)
    def range_proxie(self,start,stop):
        return self.db.zrange(REDIS_KEY,start,stop)










