# -*- encoding: utf-8 -*-
import pandas, re


class WashTool:

    def __init__(self):
        self.file_name = input("输入文件名(不带后缀)：") + '.xlsx'
        self.df = pandas.DataFrame(pandas.read_excel(self.file_name))

    def correct_date(self):
        zhongwen = re.compile(r'[\u4e00-\u9fa5]', re.S) # 中文
        number = re.compile(r'[0-9]+(\.[0-9]{0,3})?', re.S) # 小数
        # date = re.compile(r'^\d{4}-\d{1,2}-\d{1,2}', re.S) # 日期
        # url = re.compile(r' ^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$', re.S) # url
        # html = re.compile(r'<(\S*?)[^>]*>.*?</\1>|<.*? /> ', re.S) # html标签
        # ip = re.compile(r'\d+\.\d+\.\d+\.\d+', re.S) # ip
        self.df['数值'] =  self.df['信息'].apply(lambda x: zhongwen.sub('', x))
        self.df['单位'] =  self.df['信息'].apply(lambda x: number.sub('', x))
        self.df.to_excel('话题分析/'+self.file_name, index = False)
        
if __name__ == '__main__':
    WashTool().correct_date()
    print(">>>>>>>>>>>All Done!<<<<<<<<<<")