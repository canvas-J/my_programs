# -*- coding:utf8 -*-
import os

class RenameTool():

    def __init__(self):
        self.path = 'your path'

    def rename(self):
        f_list = os.listdir(self.path)
        f_count = len(f_list)
        i = 1001
        for item in f_list:
            src = os.path.join(os.path.abspath(self.path), item)
            if item.endswith('.jpg'):                
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.jpg')
            elif item.endswith('.png'):
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.png')
            elif item.endswith('.jpeg'):
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.jpeg')
            elif item.endswith('.gif'):
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.gif')
                try:
                    os.rename(src, dst)
                    print('converting {0} to {1} ...'.format(src, dst))
                    i += 1
                except:
                    continue                 
        print('total {} to rename'.format(f_count))

if __name__ == '__main__':
    demo = RenameTool()
    demo.rename()