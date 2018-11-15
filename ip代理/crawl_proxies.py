from proxies_url import *
from spider import get_page
from bs4 import BeautifulSoup
import time
import json
import re
class ProxyMetaClass(type):
    def __new__(cls,class_name,futer_name,attrs):
        count = 0
        attrs["__Proxies__"] = []
        for name,value in attrs.items():
            if "crawl_" in name:
                attrs["__Proxies__"].append(name)
                count += 1
        attrs["__ProxiesCount__"] = count
        return type.__new__(cls,class_name,futer_name,attrs)
class Crawler(object,metaclass=ProxyMetaClass):
    def get_proxies(self,callback):
        proxies = []
        for proxie in eval("self.{}()".format(callback)):
            print(f"正在抓取代理:{proxie}")
            proxies.append(proxie)
        return proxies
    def crawl_url2(self,url = url2,page = 6):
        """从89ip抓取代理"""
        realurl = url
        for i in range(1, page + 1):
            try:
                url = f"{realurl}_{i}.html"
                print(f"正在从{url}抓取代理")
                html = get_page(url)
                time.sleep(5)
                soup = BeautifulSoup(html, 'lxml')
                soup = soup.find("tbody")
                for tr in soup.find_all("tr"):
                    td = tr.find_all("td")
                    proxie = {}
                    proxie["http"] = ":".join((td[0].string.strip(), td[1].string.strip()))
                    proxie = json.dumps(proxie)
                    yield proxie
            except:
                continue
    def crawl_url5(self,url=url5):
        """从66ip抓取代理"""
        print(f"正在从{url}抓取代理")
        html = get_page(url)
        if html:
            ip = re.compile(r"((1?\d?\d.|2[0-4]\d.|25[1-5].){3}(1?\d?\d|2[0-4]\d|25[1-5]):\d+)")
            for i in re.finditer(ip, html):
                proxie = {}
                proxie["http"] = i.group(1)
                yield json.dumps(proxie)
        else:
            self.crawl_url5()
    def crawl_url6(self,url=url6):
        """从http://ip.seofangfa.com抓取代理"""
        print(f"正在从{url}抓取代理")
        try:
            html = get_page(url)
            soup = BeautifulSoup(html, 'lxml')
            soup = soup.find("table", class_="table")
            tbody = soup.find("tbody")
            for tr in tbody.find_all("tr"):
                proxie = {}
                td = tr.find_all("td")
                proxie["http"] = ":".join((td[0].text.strip(), td[1].text.strip()))
                yield json.dumps(proxie)
        except:
            self.crawl_url6()
    def crawl_url7(self,url=url7, page=5):
        """从http://ip.jiangxianli.com/抓取代理"""
        print(f"正在从{url}抓取代理")
        for i in range(1, page + 1):
            try:
                params = {"page": i}
                html = get_page(url, params=params)
                time.sleep(5)
                soup = BeautifulSoup(html, 'lxml')
                tbody = soup.find("tbody")
                for tr in tbody.find_all("tr"):
                    td = tr.find_all("td")
                    proxie = {}
                    proxie[(td[4].text.strip()).lower()] = ":".join((td[1].text.strip(), td[2].text.strip()))
                    yield json.dumps(proxie)
            except:
                continue














