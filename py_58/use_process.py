#-*- coding: UTF-8 -*-
from multiprocessing import Pool
from channel_extract  import channel_list
from parsing  import get_links_from
from parsing import  get_item_info
def get_all_links_from(channel):
    for i in range(1,100):#把所有网页链接爬取下来
        get_links_from(channel,i,1)
if __name__ == '__main__':
    pool = Pool() #进程池
    pool.map(get_all_links_from,channel_list.split())
    #把后面的列表中的地址依次放入 第一个函数中运行
