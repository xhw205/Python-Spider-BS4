#-*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
start_url = 'http://bj.ganji.com/wu/'
url_host = 'http://bj.ganji.com'

def get_index_url(url):
    # url = start_url
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('.fenlei > dt > a')
    for link in links:
        page_url = url_host + link.get('href')
        print(page_url)

channel_list = '''
http://bj.ganji.com/jiaju/
http://bj.ganji.com/rirongbaihuo/
http://bj.ganji.com/shouji/
http://bj.ganji.com/jiadian/
http://bj.ganji.com/ershoubijibendiannao/
http://bj.ganji.com/diannao/
http://bj.ganji.com/shuma/
http://bj.ganji.com/laonianyongpin/
'''
