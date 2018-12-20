import os
import shutil
import sys
from tkinter import *

def organize():
    destination = var1.get()
    backup = var2.get()
    path = os.getcwd()                              # 当前目录

    for root, dirs, files in os.walk(path):       # 获取所有路径下的路径/文件夹/文件名
        if len(files) != 0:
            for file in files:                      # 这一路径中遍历所有文件
                new = root + '/' + file
                ext = file.split('.')[-1]            # 获取后缀
                dest = destination + '/all_' + ext  # 新文件夹名字（后缀） 
                if not os.path.exists(dest):        # 不存在就创建
                    os.makedirs(dest)
                if root != dest:
                    if not os.path.exists(dest+'/'+file):     # 直接路径不再移动
                        if backup == 'yes':
                            shutil.copy(new, dest)                    
                        else:
                            shutil.move(new, dest)
    window.destroy()  # destory()[部分破坏]会报错!
    print("It's done!")


window = Tk()
window.title("organize")

L1 = Label(window,text = 'Destination:').grid(column = 0,row = 0)
var1 = StringVar()
var1.set("/home/jingang/图片")
E1 = Entry(window,textvariable = var1, bd = 2).grid(column = 1,row = 0)

L2 = Label(window,text = 'Backup:').grid(column = 0,row = 1)
var2 = StringVar()
var2.set("yes")
E2 = Entry(window,textvariable = var2, bd = 2).grid(column = 1,row = 1)

Button1 = Button(window,text = "RunOrganize",command=organize).grid(column = 1,row = 2)
window.mainloop()