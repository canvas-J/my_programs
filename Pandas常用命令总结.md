# 读取文件
self.df = pd.DataFrame(pd.read_excel(self.file_name))
self.df = pd.DataFrame(pd.read_csv(self.file_name))
# 去除空格
self.df['最低温'] = self.df['最低温'].apply(lambda x: str(x).strip())
self.df['最低温'] = self.df['最低温'].map(str.strip)
# 获取切片字段为新列 
self.df['小时'] =  self.df['发布日期'].apply(lambda x:str(x)[17:19].split(':')[0] if len(str(x))>2 else 0)
# 删除指定列 
self.df.drop(self.df.columns[8], axis=1, inplace=True)
self.df.drop(['字段10'], axis=1, inplace=True)
# 拆分，取第一部分
self.df['最低温'] = self.df['温度'].str.split('/', expand=True)[0]
# 移动列
to_drop = self.df.pop(c_name)
self.df.insert(num, c_name, to_drop)
# 新建空列
self.df['最低温'] = np.nan
# 重命名列
self.df.rename(columns={'温度':'最高温'}, inplace = True)
# 遍历函数，生成列表，转换为新列
self.df['真正发布日期'] = np.array(list(map(lambda x,y,z:self.do_merchant(x,y,z),self.df['更新时间'],self.df['小时'],self.df['发布日期'])))
# 输出为文件
self.df.to_excel(self.file_name, index = False)
self.df.to_csv(self.file_name, index = False)
# 重设索引
self.df.reset_index()
# loc函数按标签值进行提取，iloc按位置进行提取，ix可以同时按标签和位置进行提取
# 按行提取
self.df.ix[1303503]
# 按列提取
self.df.ix[:,'emp_length']
# 汇总多个单元格的值
self.df.ix[[1303503,1298717],'loan_amnt'].sum()
# 查询对应时间数据
self.df['2016-03']
# 一月到五月 
self.df['2016-01':'2016-05']
# 匹配13.5/10类型
self.df['name'].str.extract(r'(\d+\.?\d*\/\d+)', expand=False)
# 匹配12:20类型
self.df['name'].str.extract(r'(\d+\:\d+)', expand=False)
# 查找
self.df['name'].str.contains('london')
# 替换
self.df['name'].str.replace('当前时间', '') 
# 多列赋值
def myFun(x):
    return x+10, x*10
df['add_10'], df['mul_10'] = zip(*df['val'].apply(myFun)) # 解压输出两个列表
# 连接字符
pd.concat(objs,axis=0,join='outer',join_axes=None,ignore_index-False,keys=None,levels=None,verify_integrity=False,copy=True)
一般使用后要跟上(否则序号会有错误)：result = result.reset_index(drop=True)
* objs:用来保存需要用来进行连接的Series/DataFrame，可以是列表或者dict类型 
* axis表示希望进行连接的轴向，默认我0，也就是纵向拼接 
* join有多个选择，inner,outer,这里默认值是outer,下面会根据实例来比较下 
* join_axes默认为空，可以设置值指定为其他轴上使用的索引 
* ignore_index，连接后原来两个DF的index值会被保存，如果该索引没有实际的意义可以设置为True来进行重分配index号
append
df_inner = pd.merge(df,df1,how='inner')  # 匹配合并，交集
df_left = pd.merge(df,df1,how='left')    # 左连接
df_right = pd.merge(df,df1,how='right')  # 右连接
df_outer = pd.merge(df,df1,how='outer')  # 并集
# 去除重复
datalist = result.drop_duplicates(subset=['bu_links', 'c_address', 'c_name', 'c_product', 'co_links'], keep='first', inplace=False)
* subset : column label or sequence of labels, optional 用来指定特定的列，默认所有列
* keep : {‘first’, ‘last’, False}, default ‘first’ 删除重复项并保留第一次出现的项
* inplace : boolean, default False 是直接在原来数据上修改还是保留一个副本
# 某列格式
self.df['B'].dtype
# 使用均值填充列
self.df['prince'].fillna(df['prince'].mean())
# 新建标记
df_inner['group'] = np.where(df_inner['price'] > 3000,'high','low')
df_inner.loc[(df_inner['city'] == 'beijing') & (df_inner['price'] >= 4000), 'sign']=1
# 使用“与”进行筛选
df_inner.loc[(df_inner['age'] > 25) & (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']]
# 使用“或”进行筛选
df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']].sort(['age']) 
# 使用“非”条件进行筛选
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id']) 
# 对筛选后的数据按city列进行计数
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id']).city.count()
# 使用query函数进行筛选
df_inner.query('city == ["beijing", "shanghai"]')
# 对筛选后的结果按prince进行求和
df_inner.query('city == ["beijing", "shanghai"]').price.sum()