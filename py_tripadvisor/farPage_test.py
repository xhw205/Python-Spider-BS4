#-*- coding:utf-8 -*-
import  time
import requests
from bs4 import BeautifulSoup
import Mobile_farPage
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-c47-New_York_City_New_York.html'
urls = ['http://www.tripadvisor.cn/Attractions-g60763-Activities-c47-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]#列表解析式
def get_attraction(url,data = None):
    wb_data=requests.get(url)
    time.sleep(2)#间隔
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.listing_title')#得到所有的带标题信息的a标签
    #imgs = soup.select('img[width="160"]')#爬取图片许多网站做了保护措施，使得爬到的图片链接地址都一样，这显然是不对的.
    imgs = Mobile_farPage.get_url(url)#调用外部函数，采用模拟手机端页面爬取到正确的路径
    cates = soup.select('div.p13n_reasoning_v2')
#装到字典
    for title,img,cate in zip(titles,imgs,cates):
        data = {
            'title':title.get_text(),
            'img':img.get('data-thumburl'),
            'cate':list(cate.stripped_strings),
        }
        print repr(data).decode("unicode–escape")
get_attraction(url)
#爬取下30页的内容
for single_url in urls:
    get_attraction(single_url)
'''
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
    'Cookie':'SINAGLOBAL=1525822880205.785.1467604818310; UM_distinctid=15ae6c89e893-0ecfeac27f5cb6-5e4f2b18-100200-15ae6c89e8b9f; login_sid_t=6ede91b896a846033818aac2e209db7b; YF-Ugrow-G0=ad83bc19c1269e709f753b172bddb094; YF-V5-G0=69afb7c26160eb8b724e8855d7b705c6; WBStorage=02e13baf68409715|undefined; _s_tentry=www.baidu.com; UOR=www.canon.com.cn,widget.weibo.com,www.baidu.com; Apache=2117899597521.9905.1491280913561; ULV=1491280913731:13:1:1:2117899597521.9905.1491280913561:1490007625417; SSOLoginState=1491280932; wvr=6; YF-Page-G0=416186e6974c7d5349e42861f3303251; SUB=_2A25151TXDeRhGeNG71sV9yvPzDSIHXVWlcEfrDV8PUJbmtBeLULikW-BSkbEqjWiYZp5f4DJcIA1sc_lbg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whr0XnIu2Jg1QUDdGMfSaIU5JpX5o2p5NHD95Qf1hB4ShMfe0MRWs4DqcjG-cyyqcvod7tt; SUHB=06Z1YQbX0VOgSY; ALF=152281693

#print repr(cates).decode("unicode–escape")
#print repr(titles).decode("unicode–escape")#防止爬取内容乱码
'''