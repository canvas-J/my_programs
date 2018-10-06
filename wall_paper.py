# -*- coding:utf-8 -*-
import requests, datetime
from bs4 import BeautifulSoup as bs

headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
img_list = []
urls = ['http://cn.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=100']
for i in range(1, 6):
    urls.append('http://cn.bing.com/HPImageArchive.aspx?format=xml&idx={}&n=100'.format(i))
for j,url in enumerate(urls):
    response = requests.get(url, headers=headers)
    context = response.content.decode('utf-8')
    soup = bs(context, 'lxml')
    img_link = "http://cn.bing.com/" + soup.select_one("images > image > url").string
    with open("D:/02日常抓取/bing壁纸/"+str(datetime.datetime.now().microsecond)+str(j)+".jpg", 'wb') as f:
        img = requests.get(img_link, headers=headers)
        if img:
            f.write(img.content)
    print('已保存了{}张图片'.format(j+1))
