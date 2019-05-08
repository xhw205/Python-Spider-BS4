#-*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random
client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
item_info = ganji['item_info']

headers  = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

# http://www.xicidaili.com/
#为了防止封ip
proxy_list = [
    'http://222.52.142.242:8080',
    'http://124.239.177.85:8080',
    'http://182.92.207.196:3128',
    ]
proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}
# spider 1
def get_links_from(channel, pages, who_sells='o',proxies=proxies):#获取链接
    # o for personal a for merchant
    list_view = '{}{}{}/'.format(channel, str(who_sells), str(pages))#代表如下格式--http://bj.ganji.com/ershoubijibendiannao/o3/
    wb_data = requests.get(list_view,headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if who_sells=='a':
        if soup.find('ul', 'pageLink'):
            for link in soup.select('.ft-tit'):
                item_link = link.get('href')
                if str(item_link).find("ganji")!=-1:#排除一些广告网站
                    url_list.insert_one({'url': item_link})#存入数据库
                    print(item_link)
        else:
            pass
    else:
        if soup.find('ul', 'pageLink'):
            for link in soup.select('td.t a'):
                item_link = link.get('href').split('?')[0]
                url_list.insert_one({'url': item_link})#存入数据库
                print(item_link)
        else:
        # It's the last page !
            pass
# spider 2
def zhuanzhuan(url,data=None):
    try:
        wb_data = requests.get(url,headers=headers)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        data={
            'title':soup.title.text.strip(),
            'price':soup.select('span > i')[0].text,
            'area':soup.select('div.palce_li > span > i')[0].text,
            'url':url
        }
        item_info.insert_one(data)
        print repr(data).decode("unicode–escape")
    except IndexError:
        pass
def get_item_info_from(url,data=None):#获取具体网页的信息
    wb_data = requests.get(url,headers=headers)
    if wb_data.status_code == 404:
        pass
    else:
        if str(url).find("zhuanzhuan")!=-1:
            zhuanzhuan(url)
        else:
            try:
                soup = BeautifulSoup(wb_data.text, 'lxml')
                data = {
                    'title':soup.title.text.strip(),
                    'price':soup.select('.f22.fc-orange.f-type')[0].text.strip(),
                    'pub_date':soup.select('.pr-5')[0].text.strip().split(' ')[0],
                    'area':list(map(lambda x:x.text,soup.select('ul.det-infor > li:nth-of-type(3) > a'))),
                    'cates':list(soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].stripped_strings),
                    'url':url
                }
                item_info.insert_one(data)
                print repr(data).decode("unicode–escape")
            except:
                pass
#get_item_info_from('http://zhuanzhuan.ganji.com/detail/852210391674109959z.shtml')
