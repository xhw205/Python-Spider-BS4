#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests
import time
def get_links_from(who_sells):
    urls = []
    list_view = 'http://bj.58.com/pbdn/{}/pn2/'.format(str(who_sells))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('td.t a.t'):
        if who_sells==0: #0是个人
            if str(link).find("zhuanzhuan") != -1:
                urls.append(link.get('href').split('?')[0])
        else:#1代表商家
            if str(link).find("html") != -1:
                urls.append(link.get('href').split('?')[0])
    return urls
# def get_views_from(url):
#     id = url.split('/')[-1].strip('x.shtml')
#     api = 'http://jst1.58.com/counter?infoid={}'.format(id)
#     #58的查询接口
#     js = requests.get(api)
#     views = js.text.split('=')[-1]
#     return views
def get_item_info_store(who_sells=1):
    urls = get_links_from(who_sells)
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        data = {
            'title':soup.title.text,
            'price':soup.select('.price')[0].text,
            'area' :list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span','c_25d') else None,
            'date' :soup.select('.time')[0].text,
            'cate' :'Storesale',
        }
        #return data
        print repr(data).decode("unicode–escape")
def get_item_info_person(who_sell=0):
    urls = get_links_from(who_sell)
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        data = {
            'title':soup.title.text,
            'price':soup.select('div.price_li > span > i')[0].text,
            'area' :list(soup.select('div.palce_li > span > i')[0].stripped_strings),
            # 'views':get_views_from(url)
        }
        #return data
        print repr(data).decode("unicode–escape")
def get_item(who_sell):
    if who_sell==0:
        get_item_info_person()
    else:
        get_item_info_store()
get_item(0)#个人

get_item(1)#商家