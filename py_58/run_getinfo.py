#-*- coding: UTF-8 -*-
import pymongo
from multiprocessing import Pool
from parsing import  get_item_info
client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
urls = ceshi['url_list2']
#item_info = ceshi['item_info3']
#item_info_person = ceshi['item_info3_per']
for item in urls.find():
    get_item_info(item['url'])