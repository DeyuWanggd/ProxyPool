
from proxies_url import *
from config import HEADERS
from spider import get_page
from bs4 import BeautifulSoup
import time
import json
import re
def crawl_url2(url=url2,page =5):
    for i in range(1,page+1):
        time.sleep(5)
        url = f"{url}_{page}.html"
        print(url)
        html = get_page(url)
        soup = BeautifulSoup(html, 'lxml')
        soup = soup.find("tbody")
        for tr in soup.find_all("tr"):
            td = tr.find_all("td")
            proxie = {}
            proxie['http'] = ":".join((td[0].string.strip(), td[1].string.strip()))
            proxie = json.dumps(proxie)
            yield proxie
def crawl_url5(url=url5):
    html = get_page(url)
    ip = re.compile(r"((1?\d?\d.|2[0-4]\d.|25[1-5].){3}(1?\d?\d|2[0-4]\d|25[1-5]):\d+)")
    for i in re.finditer(ip,html):
        proxie = {}
        proxie["http"] = i.group(1)
        yield proxie
def crawl_url6(url = url6):
    html = get_page(url)
    soup = BeautifulSoup(html,'lxml')
    soup = soup.find("table",class_ = "table")
    tbody = soup.find("tbody")
    for tr in tbody.find_all("tr"):
        proxie = {}
        td = tr.find_all("td")
        proxie["http"] = ":".join((td[0].text.strip(),td[1].text.strip()))
        print(proxie)
def crawl_url7(url = url7,page = 5):
    for i in range(1,page+1):
        params = {"page":i}
        html = get_page(url,params=params)
        time.sleep(5)
        soup = BeautifulSoup(html,'lxml')
        tbody = soup.find("tbody")
        for tr in tbody.find_all("tr"):
            td = tr.find_all("td")
            proxie = {}
            proxie[(td[4].text.strip()).lower()] = ":".join((td[1].text.strip(),td[2].text.strip()))
            yield proxie
















