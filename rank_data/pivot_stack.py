# -*- coding: utf-8 -*-
import pandas as pd

def split():
    """
    拆分数据，将数据拉长
    """
    result = data.set_index(['年份','地区']).stack()
    result.to_excel('ex.xlsx', encoding='GB18030')

def povit_da():
    """
    透视数据，将数据压扁
    """
    data['date'].astype(str) # 强制转换格式
    result = data.pivot_table(index=['date','type'], columns=['name',], values='value',
                        aggfunc=sum, fill_value=0, margins=True) # len mean
    result.to_excel('ex.xlsx', encoding='GB18030')

def merge_on_key():
    """
    匹配，并增加新表格数据
    """
    new = pd.read_excel('new.xlsx', encoding='GB18030')
    result = pd.merge(data, new, on=['年份','地区'], how='left', sort=False)
    result.to_excel('ex.xlsx', encoding='GB18030', index=False)

def concat_data():
    """
    合并同类数据
    """
    # 单个文件
    new = pd.read_excel('new.xlsx', encoding='GB18030')
    result = pd.concat([data, new], ignore_index=True, copy=True)
    # 批量合并
    # excel_list = glob.glob('file/*.xlsx')
    # frames = []
    # for c_name in excel_list:
    #     frames.append(pd.read_excel(c_name, encoding="gb18030"))
    # result = pd.concat(frames, ignore_index=True, copy=True)
    result.reset_index(drop=True) # 合并后需要重设索引
    result = result[pd.isna(result['年份']) == False] # 去除该列为空的行
    result = result.drop_duplicates(keep='first', inplace=False) # 去重，取第一个值
    # import numpy as np
    # result['flag'] = np.where(result['年份'] > 2000, '近年', '更早') # 备注数据信息
    result.to_excel('ex.xlsx', encoding='GB18030', index=False)

def table_apart():
    """
    将数据按某列拆分为多张表
    """
    keys = data['地区'].dropna().unique()
    writer = pd.ExcelWriter('ex.xlsx')
    for na in keys:
        result = data[data['地区'] == na]
        result.to_excel(writer, sheet_name=na, encoding='GB18030', index=False)


if __name__ == '__main__':
    data = pd.read_excel('example.xlsx', encoding='GB18030')
    # data = pd.read_csv('example.csv', encoding='GB18030')
    # split()
    povit_da()
    # concat_data()
    # merge_on_key()
    # table_apart()