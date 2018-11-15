import asyncio
import aiohttp
from db import db
from config import *
import time
import json
class Tester(object):
    def __init__(self):
        self.db = db()
    async def test_proixe(self,proxie):
        if isinstance(proxie,bytes):
            proxie = proxie.decode("utf-8")
        conn = aiohttp.TCPConnector(verify_ssl=False)
        proxie = json.loads(proxie)
        test_proxie = json.dumps(proxie.copy())
        a,b = proxie.popitem()
        proxie = "{}://{}".format(a,b)
        try:
                async with aiohttp.ClientSession(connector=conn) as session:
                    async with session.get(TEST_URL,proxy=proxie,timeout = 5,allow_redirects=False,headers=HEADERS) as response:
                        response.raise_for_status()
                        self.db.update_proxie(test_proxie)
                        print(proxie,"代理可用")
        except:
            #self.db.del_proxie(test_proxie)
            error_proxies.append(test_proxie)
            print(proxie,"代理异常")
    def run(self):
        global error_proxies
        error_proxies = []
        print("测试器开始执行")
        count = self.db.count_proxie()
        print(f"当前共有{count}个代理")
        for i in range(0,count,TEST_COUNT):
            try:
                start = i
                stop = min(count,i+TEST_COUNT)
                proxies = self.db.range_proxie(start=start,stop=stop)
                print(f"正在测试从{start+1}-{stop}的代理")
                event_loop = asyncio.get_event_loop()
                tasks = [self.test_proixe(proxie) for proxie in proxies]
                event_loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)
            except Exception as reason:
                print("测试器出错",reason)
                continue
        for i in error_proxies:
            self.db.del_proxie(i)



