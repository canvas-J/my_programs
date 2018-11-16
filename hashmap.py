# -*- coding:utf-8 -*-


class LineMap(object):
    """ 
    线性表结构：我们可以在使用add添加元素时让items列表保持有序，而在使用get时采取二分查找方式，时间复杂度为O(log n)。 
    然而往列表中插入一个新元素实际上是一个线性操作，所以这种方法并非最好的方法。
    同时，我们仍然没有达到常数查找时间的要求。
    """
    def __init__(self):
         self.items = []
  
    def add(self, k, v):  
        self.items.append((k,v))

    def get(self, k): 
        for key, value in self.items:      
            if key == k:      # 键存在，返回值，否则抛出异常
                return value
        raise KeyError



class TableMap(object):
    '''
    将总查询表分割为若干段较小的列表，比如100个子段。
    通过hash函数求出某个键的哈希值，再通过计算，得到往哪个子段中添加或查找。
    相对于从头开始搜索列表，时间会极大的缩短。
    '''
    def __init__(self,n=100):
        '''
        利用LineMap对象作为子表，建立更快的查询表
        '''
        self.maps = []          # 总表格
        for i in range(n):      # 根据n的大小建立n个空的子表
            self.maps.append(LineMap())
      
    def find_map(self,k):       # 通过hash函数计算索引值
        index = hash(k) % len(self.maps)
        return self.maps[index] # 返回索引子表的引用     
 
    
    def add(self, k, v):
        '''
        寻找合适的子表（LineMap对象）,进行添加和查找
        '''
        m = self.find_map(k)        
        m.add(k,v)
     
    def get(self, k):
        m = self.find_map(k)
        return m.get(k)


class HashMap(object):
    '''
    由于对n个元素进行add操作的总时间与n成比例，所以每次add的平均时间就是一个常数！
    '''
    def __init__(self):
        '''
        初始化总表为，容量为2的表格（含两个子表）
        '''
        self.maps = TableMap(2)
        self.num = 0        # 表中数据个数
      
    def get(self,k):        
        return self.maps.get(k)
      
    def add(self, k, v):
        '''
        若当前元素数量达到临界值（子表总数）时，进行重排操作
        对总表进行扩张，增加子表的个数为当前元素个数的两倍！
        '''
        if self.num == len(self.maps.maps): 
            self.resize()
         
        # 往重排过后的 self.map 添加新的元素
        self.maps.add(k, v)
        self.num += 1
         
    def resize(self):
        '''
        重排操作，添加新表, 注意重排需要线性的时间
        先建立一个新的表,子表数 = 2 * 元素个数
        '''
        new_maps = TableMap(self.num * 2)
         
        for m in self.maps.maps:  # 检索每个旧的子表
            for k,v in m.items:   # 将子表的元素复制到新子表
                new_maps.add(k, v)
         
        self.maps = new_maps      # 令当前的表为新表