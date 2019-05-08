#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
start_url = 'http://bj.58.com/sale.shtml'
url_host = 'http://bj.58.com'
def get_channel_urls(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        page_url = url_host + link.get('href')
        print page_url
#get_channel_urls(start_url)
    # http://bj.58.com/shouji/
    # http://bj.58.com/tongxunyw/
    # http://bj.58.com/danche/
    # http://bj.58.com/diandongche/
    # http://bj.58.com/diannao/
    # http://bj.58.com/bijiben/
    # http://bj.58.com/pbdn/
    # http://bj.58.com/diannaopeijian/
    # http://bj.58.com/zhoubianshebei/
    # http://bj.58.com/shuma/
    # http://bj.58.com/mpsanmpsi/
    # http://bj.58.com/youxiji/
    # http://bj.58.com/jiadian/


channel_list = '''
    http://bj.58.com/shouji/
    http://bj.58.com/tongxunyw/
    http://bj.58.com/danche/
    http://bj.58.com/diandongche/
    http://bj.58.com/diannao/
    http://bj.58.com/bijiben/
    http://bj.58.com/pbdn/
    http://bj.58.com/diannaopeijian/
    http://bj.58.com/zhoubianshebei/
    http://bj.58.com/shuma/
    http://bj.58.com/mpsanmpsi/
    http://bj.58.com/youxiji/
    http://bj.58.com/jiadian/
    '''