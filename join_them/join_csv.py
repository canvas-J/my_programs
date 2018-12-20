# -*- coding: utf-8 -*-
import os
import pandas as pd
import glob

class MerageTool:

    def merage_csv():
        csv_list = glob.glob('file/*.csv')
        print(u'共发现{}个CSV文件'.format(len(csv_list)))
        print(u'正在处理............')
        frames = []
        for c_name in csv_list:
            frames.append(pd.read_csv(c_name, encoding="gb18030", low_memory=False))
        result = pd.concat(frames)
        result = result.reset_index(drop=True)
        print(u'>>>>>>合并完毕！<<<<<<')
        datalist = result.drop_duplicates(subset=['bu_links', 'c_address', 'c_name', 'c_product', 'co_links'], keep='first', inplace=False)
        datalist.to_csv("result.csv", encoding="gb18030")
        print(u'>>>>>>去重完毕！<<<<<<')

    def merage_excel():
        excel_list = glob.glob('file/*.xlsx')
        print(u'共发现{}个excel文件'.format(len(excel_list)))
        print(u'正在处理............')
        frames = []
        for c_name in excel_list:
            frames.append(pd.read_excel(c_name, encoding="gb18030"))
        result = pd.concat(frames)
        result = result.reset_index(drop=True)
        print(u'>>>>>>合并完毕！<<<<<<')
        datalist = result.drop_duplicates(subset=['bu_links', 'c_address', 'c_name', 'c_product', 'co_links'], keep='first', inplace=False)
        datalist.to_csv("result.xlsx", encoding="gb18030")
        print(u'>>>>>>去重完毕！<<<<<<')

if __name__ == '__main__':
    MerageTool.merage_csv()
    # MerageTool.merage_excel()