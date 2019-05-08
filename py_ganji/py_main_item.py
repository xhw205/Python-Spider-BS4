#-*- coding: UTF-8 -*-
import pymongo
from multiprocessing import Pool
from page_parsing import get_item_info_from,url_list,item_info,get_links_from
from channel_extracing import channel_list
client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ganji']
urls = ceshi['url_list']
for item in urls.find():
    get_item_info_from(item['url'])

# db_urls = [item['url'] for item in url_list.find()]
# index_urls = [item['url'] for item in item_info.find()]
# x = set(db_urls)
# y = set(index_urls)
# rest_of_urls = x-y
# for d in x:
#     print (d)







