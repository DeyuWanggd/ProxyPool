from config import *
from getter import Getter
from tester import Tester
from multiprocessing import Process
from api import app
import time
from db import db
class Scheduer(object):
    def process_getter(self):
        '''获取器执行子进程'''
        getter = Getter()
        redis = db()
        while True:
            if redis.count_proxie() < MAXPOOL:
                getter.run()
                time.sleep(GETTER_CYCLE)
            else:
                print("代理池已经达到最大容量")
                break
    def process_tester(self):
        '''测试器执行子进程'''
        tester = Tester()
        while True:
            tester.run()
            time.sleep(TESTER_CYCLE)
    def process_api(self):
        '''api子进程'''
        app.run(API_HOST, API_PORT)
    def run(self):
        print("调度器开始运行")
        if GETTER:
            getter_process = Process(target=self.process_getter)
            getter_process.start()
        if TESTER:
            tester_process = Process(target=self.process_tester)
            tester_process.start()
        if API:
            api_process = Process(target=self.process_api)
            api_process.start()
if __name__ == "__main__":
    s = Scheduer()
    s.run()


