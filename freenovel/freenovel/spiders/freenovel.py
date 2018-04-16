# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from freenovel.items import FreenovelItem


class CleanTool:   
    removeImg = re.compile('<img.*?>')                  #去除img标签,7位长空格
    removeAddr = re.compile('<a.*?>|</a>')              #删除超链接标签
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')      #把换行的标签换为\n
    replaceTD= re.compile('<td>')                       #将表格制表<td>替换为\t
    replacePara = re.compile('<p.*?>')                #把段落开头换为\n加空两格
    replaceBR = re.compile('<br><br>|<br>')             #将换行符或双换行符替换为\n
    removeExtraTag = re.compile('<.*?>')                #将其余标签剔除
    remove01 = re.compile(r'\\u3000\\u3000')
    remove02 = re.compile(r'\u3000\u3000')
    remove03 = re.compile('\',')
    remove04 = re.compile('\'')
    remove05 = re.compile(r'"')

    list2remove = [removeImg, removeAddr, replaceLine, replaceTD, replacePara, replaceBR, 
                removeExtraTag, remove01, remove02, remove03, remove04, remove05
    ]

    def replace(self,x):
        for i in self.list2remove:
            x = re.sub(i, "", x)  
        return x.strip()

class FreenovelSpider(scrapy.Spider):
    name = 'freenovel'
    allowed_domains = ['readnovel.com']
    start_urls = ['https://www.readnovel.com/free/']

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',\
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',\
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'
    }

    def __init__(self):
        self.tool = CleanTool()

    def parse(self, response):
        # print(response.text)
        next_page = response.xpath('//h4/a/@href').extract()
        for next_url in next_page:
            next_page = 'https://www.readnovel.com' + next_url + '#Catalog'
            yield scrapy.Request(next_page, headers=self.headers, callback=self.parse_chapter)

    def parse_chapter(self, response):
        # print(response.text)
        urls = response.xpath('//ul[@class="cf"]/li/a/@href').extract()
        for i in range(7, len(urls)):
            url = "https:" + urls[i]
            yield scrapy.Request(url, headers=self.headers, callback=self.parse_content)

    def parse_content(self, response):
        # print(response.text)
        item = FreenovelItem()
        item['name'] = response.xpath('//a[@class="act"]/text()').extract_first()
        item['author'] = response.xpath('//h2/a/text()').extract_first()
        item['chapter'] = response.xpath('//h3[@class="j_chapterName"]/text()').extract_first()
        x = response.xpath('//div[@class="read-content j_readContent"]/p/text()').extract()
        x1 = str()
        for i in x:
            x1 += str(i)
        item['content'] = self.tool.replace(str(x1))
        yield item