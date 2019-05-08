#-*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import random
import pymongo
client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
url_list = ceshi['url_list2']
item_info = ceshi['item_info3']
item_info_person = ceshi['item_info3_per']
#spider1
# http://www.xicidaili.com/
#为了防止封ip
headers  = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER',
}
proxy_list = [
    'http://222.52.142.242:8080',
    'http://124.239.177.85:8080',
    'http://182.92.207.196:3128',
    ]
proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}
def get_links_from(channel, pages, who_sells=0,proxies=proxies):#获取链接存入数据库
    #http://bj.58.com/diannao/0/pn2/
    list_view = '{}{}/pn{}/'.format(channel, str(who_sells), str(pages))
    wb_data = requests.get(list_view,headers=headers)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]#截取网址正确地址
            if str(link).find("zhuanzhuan") != -1:#找到了(58同城二手网,zhuanzhuan代表个人用户)
                url_list.insert_one({'url':item_link})
                print repr(item_link).decode("unicode–escape")
            else:
                if str(link).find("shtml") != -1:
                    url_list.insert_one({'url':item_link})
                    print repr(item_link).decode("unicode–escape")
    else:
        pass
#spider2
def zhuanzhuan(url,data=None):
    try:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')#404页面自动跳过
        ti = soup.select('span.soldout_btn')
        if str(ti).find("\u4e0b\u67b6")!=-1:#此编码代表下架
             pass
        else:
            title1 = soup.title.text
            price1 = soup.select('div.price_li > span > i')[0].text
            area1 = list(soup.select('div.palce_li > span > i')[0].stripped_strings)
            item_info_person.insert_one({'title': title1, 'price': price1, 'area': area1, 'url': url})
            data = {#输出放到字典，为了直观
                'title':title1,
                'price':price1,
                'area' :area1,
                }
            print repr(data).decode("unicode–escape")
    except:
        pass
def get_item_info(url,data=None):
    if str(url).find("zhuanzhuan") != -1:#找到了(58同城二手网,zhuanzhuan代表个人用户)
        zhuanzhuan(url)
    else:
        try:
            wb_data = requests.get(url)
            soup = BeautifulSoup(wb_data.text,'lxml')
            #404页面自动跳过
            no_longer_exist = '404' in soup.find('script',type="text/javascript").get('src').split('/')
            if no_longer_exist:
                pass
            else:
                title1 = soup.title.text
                price1 = soup.select('span.price.c_f50')[0].text
                date1 = soup.select('.time')[0].text
                area = soup.select('.c_25d a')
                cates =  list(soup.select('div.breadCrumb.f12')[0].stripped_strings)
                quyu = soup.select('div.su_tit')
                if str(area).find('\u501f\u94b1\u4e70')!=-1:#有借钱买
                        a=list(soup.select('.c_25d a')[1].stripped_strings) if str(quyu).find('\u533a\u57df')!=-1 else None
                        if len(cates)==3:
                            item_info.insert_one({'title': title1, 'price': price1, 'pub_date': date1,'cates':cates, 'area': a, 'url': url})
                else:
                        a=list(soup.select('.c_25d a')[0].stripped_strings) if str(quyu).find('\u533a\u57df')!=-1 else None
                        if len(cates)==3:
                            item_info.insert_one({'title': title1, 'price': price1, 'pub_date': date1, 'cates':cates,'area': a, 'url': url})

                data = {#输出放到字典，为了直观
                    'title':title1,
                    'price':price1,
                    'date':date1,
                    'area':a,
                    'cates':cates
                }
                print repr(data).decode("unicode–escape")
        except IndexError:
                pass
#get_links_from('http://bj.58.com/shuma/',2,1)#存入数据库，0代表个人，1代表商家
#get_item_info('http://bj.58.com/pingbandiannao/25617951988414x.shtml')

