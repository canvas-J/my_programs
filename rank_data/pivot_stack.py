import pandas as pd

def split():
    """
    拆分数据，将数据拉长
    """
    result = data.set_index(['年份','地区']).stack()
    result.to_excel('ex.xlsx', encoding='GB18030')

def povit_ta():
    """
    透视数据，将数据压扁
    """
    data['date'].astype(str)
    result = data.pivot_table(index=['date','type'], columns=['name',], values='value',
                        aggfunc=sum, fill_value=0, margins=True) # len mean
    result.to_excel('ex.xlsx', encoding='GB18030')

if __name__ == '__main__':
    # data = pd.read_excel('example.xlsx', encoding='GB18030')
    data = pd.read_csv('example.csv', encoding='GB18030')
    # split()
    povit_ta()