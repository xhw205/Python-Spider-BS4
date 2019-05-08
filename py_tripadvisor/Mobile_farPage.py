#-*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import time
headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}
urls = ['http://www.tripadvisor.cn/Attractions-g60763-Activities-c47-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]#列表解析式
url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-c47-New_York_City_New_York.html#ATTRACTION_LIST'
def get_url(url,data = None):
    time.sleep(2)
    mb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(mb_data.text,'lxml')
    imgs=soup.select('div.missing.lazyMiss')
    return imgs
def out(url):
    for i in get_url(url):
        print(i.get('data-thumburl'))
