#-*- coding: UTF-8 -*-
#解析静态网页#
from bs4 import BeautifulSoup
data = []
path = 'f://new_index.html'

with open(path, 'r') as f:
    Soup = BeautifulSoup(f.read(), 'lxml')
    titles = Soup.select('ul > li > div.article-info > h3 > a')
    pics = Soup.select('ul > li > img')
    descs = Soup.select('ul > li > div.article-info > p.description')
    rates = Soup.select('ul > li > div.rate > span')
    cates = Soup.select('ul > li > div.article-info > p.meta-info')
for title, pic, desc, rate, cate in zip(titles, pics, descs, rates, cates):
    info = {
        'title': title.get_text(),
        'pic': pic.get('src'),
        'descs': desc.get_text(),
        'rate': rate.get_text(),
        'cate': list(cate.stripped_strings)
    }
    data.append(info)
for i in data:
    if len(i['rate']) >=3:
        print(i['title'], i['cate'])
	'''
		body > div.main-content > ul > li:nth-child(1) > img

		body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a

		body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(2)

		body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description

		body > div.main-content > ul > li:nth-child(1) > div.rate > span
	'''