# - * - coding: utf - 8 -*-
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from tkinter import *
import jieba
import random
# jieba.load_userdict("txt\userdict.txt")
# 添加用户词库为主词典,原词典变为非主词典
from wordcloud import WordCloud, ImageColorGenerator

#声名一个tk（你可以把tk理解为一个窗口）
root = Tk()
#这里填写什么，生成窗口的名字就是什么
root.title("w_cloud")


# 添加自己的词库分词
def add_word(list):
    for items in list:
        jieba.add_word(items)

def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path, 'r', encoding='utf-8')
    try:
        f_stop_text = f_stop.read( )
    finally:
        f_stop.close( )
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

def TXT2WC():

    # 获取当前文件路径
    # __file__ 为当前文件, 在ide中运行此行会报错,可改为
    # d = path.dirname('.')
    d = path.dirname(__file__)
    global stopwords_path
    # stopwords = {}
    
    isCN = 1 #默认启用中文分词
    pic_name = var1.get()
    file_name = var2.get()
    new_name = var3.get()
    back_col = var4.get()
    back_coloring_path = "file/{}".format(pic_name) # 设置背景图片路径
    text_path = 'file/{}'.format(file_name) #设置要分析的文本路径
    font_path = 'file/msyhbd.ttf' # 为matplotlib设置中文字体路径没
    stopwords_path = 'file/stopwords1893.txt' # 停用词词表
    imgname1 = "{}-Str.jpg".format(new_name)
    # imgname1 = "云图BStr{}.png".format(random.randint(1,30)) # 保存的图片名字1(只按照背景图片形状)
    imgname2 = imgname1.replace("Str", "Col")# 保存的图片名字2(颜色按照背景图片颜色布局生成)

    my_words_list = ['路明非'] # 在结巴的词库中添加新词
    back_coloring = imread(path.join(d, back_coloring_path))# 设置背景图片

    # 设置词云属性
    wc = WordCloud(font_path=font_path,  # 设置字体
                   background_color="white",  # 背景颜色
                   max_words=400,  # 词云显示的最大词数
                   mask=back_coloring,  # 设置背景图片
                   max_font_size=350,  # 字体最大值
                   random_state=42,
                   width=1366, height=768, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
                   )
    add_word(my_words_list)
    text = open(path.join(d, text_path), 'r', encoding='utf-8').read()

    if isCN:
        text = jiebaclearText(text)

    # 生成词云, 可以用generate输入全部文本(wordcloud对中文分词支持不好,建议启用中文分词),也可以我们计算好词频后使用generate_from_frequencies函数
    wc.generate(text)
    # wc.generate_from_frequencies(txt_freq)
    # txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
    # 从背景图片生成颜色值
    # 保存的图片名字1(只按照背景图片形状)
    image_colors = ImageColorGenerator(back_coloring)
    wc.to_file(path.join(d, "img/{}".format(imgname1)))         
    plt.figure()
    # 以下代码显示图片
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    # 绘制词云

    if back_col == 'n':
        pass
    else:
        # 保存的图片名字2(颜色按照背景图片颜色布局生成)
        image_colors = ImageColorGenerator(back_coloring)
        plt.imshow(wc.recolor(color_func=image_colors))
        # 保存图片
        wc.to_file(path.join(d, "img/{}".format(imgname2)))
        plt.axis("off")
        # 绘制背景图片为颜色的图片
        # plt.figure()
        # plt.imshow(back_coloring, cmap=plt.cm.gray)
        # plt.axis("off")
        plt.show()
        

def T_interface():
    # 输入框变量设置后不能马上get()获取，必须要有command响应，相当于刷新和重新获取
    
    global var1, var2, var3, var4

    #下面这些是对最开始的时候创建的tk进行行列式填充 label为文本 entry为输入框 
    L1 = Label(root,text = '使用的背景图名:').grid(column = 0,row = 0)
    var1 = StringVar()
    var1.set("pic_demo.jpg")
    E1 = Entry(textvariable = var1, bd = 2).grid(column = 1,row = 0)

    L2 = Label(root,text = '传入的文档名:').grid(column = 0,row = 1)
    var2 = StringVar()
    var2.set("file_demo.txt")
    E2 = Entry(textvariable = var2, bd = 2).grid(column = 1,row = 1)
    
    L3 = Label(root,text = '生成的文件名(不带后缀):').grid(column = 0,row = 2)
    var3 = StringVar()
    var3.set("w_cloud01")
    E3 = Entry(textvariable = var3, bd = 2).grid(column = 1,row = 2)
    
    L4 = Label(root,text = '是否按背景颜色分布显示(y/n):').grid(column = 0,row = 3)
    var4 = StringVar()
    var4.set("n")
    E4 = Entry(textvariable = var4, bd = 2).grid(column = 1,row = 3)
    
    Button1 = Button(root,text = "MAGIC",command=TXT2WC).grid(column = 1,row = 4)
    Message(root,text = '>>>>请先填充选项<<<<',aspect = 400).grid(column = 0,row = 4)
    # root.update()
    root.mainloop()

T_interface()







