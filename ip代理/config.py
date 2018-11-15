#redis数据库
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = "new_proxies"
#分数设置:
FIRST_SOCRE = 0
#头部信息
HEADERS = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Pragma':'no-cache',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
#代理池最大数量
MAXPOOL = 150
#获取器开关
GETTER = True
#测试器开关
TESTER = True
#测试地址
TEST_URL = "https://www.baidu.com"
#一次测试的数量
TEST_COUNT = 30
#网页接口开关
API = True
#API配置信息
API_HOST = '0.0.0.0'
API_PORT = 5100
#HTTP状态码
GOOD_CODE = (200,301)
#获取器循环时间
GETTER_CYCLE = 150
#测试器循环时间
TESTER_CYCLE = 150