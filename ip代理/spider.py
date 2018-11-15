import requests
from config import HEADERS
from requests.exceptions import HTTPError
from requests.exceptions import ProxyError
from requests.exceptions import ConnectTimeout
from db import db
import json

db = db()
def get_proxie():
    if db.get_proxie():
        proxie = db.get_proxie().replace("'","\"")
        if isinstance(proxie,bytes):
            proxie = proxie.decode("utf-8")
        return json.loads(proxie)
    else:
        return None
def get_page(url,headers=HEADERS,params=None):
    proxie =get_proxie()
    try:
        res = requests.get(url,headers = headers,params=params,allow_redirects = False,proxies=proxie,timeout=30)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except (ProxyError,ConnectTimeout):
        get_page(url)
    except (ConnectionError,HTTPError,TimeoutError) as reason:
        print(f'该{url}有问题,建议删除',reason)
        return None



