#-*- coding: UTF-8 -*-
from multiprocessing import Pool
from page_parsing import get_item_info_from,url_list,item_info,get_links_from
from channel_extracing import channel_list
#做

def get_all_links_from(channel):
    for i in range(1,100):#把所有网页链接爬取下来
        get_links_from(channel,i,'a')#a代表商家,o代表用户
if __name__ == '__main__':
    pool = Pool() #进程池
    pool.map(get_all_links_from,channel_list.split())


