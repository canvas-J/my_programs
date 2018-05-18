# -*- coding:utf-8 -*-


# @staticmethod  @classmethod  @property的理解
class Girlfriend:
    # 类属性
    age = 22
    sex = '女'

    # 实例化过程自动执行，添加属性
    def __init__(self, hair):
        self.hair = hair
        self.bra = 'C'

    # self形成命名空间，传递一整个实例对象（谁的，属性）约定俗成，非关键词
    def about_me(self):
        print('年芳{0}，性别{1}，身材{2}棒棒哒，一头{3}'.format(self.age, self.sex, self.size, self.hair))

    # 实例调用该方法时，不传递任何参数
    @staticmethod
    def slogan():
        print('全心全意为主人服务!')

    # 实例调用该方法时，隐式传递类，访问类的内置属性
    @classmethod
    def cls_name(cls):
        print('当前使用模具是{0}'.format(cls.__name__))

    # 通过用方法模拟类属性，来实现对类属性的功能和约束的实现
    @property
    def size(self):
        return self.bra

    # 不设置setter方法就会成为只读属性
    # 此处可以添加条件或者其它功能约束这个属性
    @size.setter
    def size(self, size):
        self.bra = size
        print('丰胸手术完成！')

# 装饰器的理解
# 能在函数的入口或出口做一些特殊的操作

# 装饰器参数
def decorator(arg_of_decorator):
    # 传入函数名
    def log(func):
        # 可以传入参数
        def wrapper(*arg, **kw):
            # 这些是包装的功能
            print 'Start %s' % func
            # 在这里使用装饰器参数arg_of_decorator 
            return func(*arg, **kw)
       return wrapper
    return log

# 面向对象，一定要把所有东西都包装起来，做到可以简单地拿来就用！！！
@decorator
def func_a(arg):
    pass

@decorator
def func_b(arg):
    pass

@decorator
def func_c(arg):
    pass