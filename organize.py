import os
import shutil
import sys

destination = sys.argv[2]       # 获取命令第一个参数
backup = sys.argv[1]
if destination == '--curr':     # 使用本目录
    destination = os.getcwd()
elif not os.path.exists(destination):   #指定目录不存在
    os.makedirs(dest)
path = os.getcwd()                      # 当前目录

for root, dirs, files in os.walk(path):# 获取所有路径下的路径/文件夹/文件名
    if len(files) != 0:
        for file in files:                  # 这一路径中遍历所有文件
            new = root + '/' + file
            ext = file.split('.')[-1]       # 获取后缀
            dest = destination + '/all_' + ext  # 新文件夹名字（后缀） 
            if not os.path.exists(dest):   # 不存在就创建
                os.makedirs(dest)
            if root != dest:
                if not os.path.exists(dest+'/'+file):               # 直接路径不再移动
                    if backup = yes:
                        shutil.copy(new, dest)                    
                    else:
                        shutil.move(new, dest)
                    # print("Moved "+new+' to '+dest) 