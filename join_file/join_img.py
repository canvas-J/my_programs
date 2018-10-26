import os, datetime, random
from PIL import Image

def add_imgPath(dirName=os.getcwd()):
    img_paths = []
    count_max = line_max * row_max
    for root,dirs,files in os.walk(dirName):
        for na in files:
            if "jpg" in na:
                img_paths.append(os.path.join(root, na))
                if len(img_paths) >= count_max:
                    break
    random.shuffle(img_paths)
    return img_paths

def join_img(img_paths):
    num = 0
    toImage = Image.new('RGBA',(img_w*line_max, img_h*row_max))
    for i in range(row_max): 
        for j in range(line_max):
            fole_head =  Image.open(img_paths[num])
            tmp_img = fole_head.resize((img_w, img_h))
            loc = (int(i % line_max * img_w), int(j % line_max * img_h))
            toImage.paste(tmp_img, loc)
            num = num + 1
            if num >= len(img_paths):
                num = 0
    print(toImage.size)
    now = datetime.datetime.now().strftime('%m-%d-%M')
    toImage.save('{}merged.png'.format(now))

if __name__ == '__main__':
    img_w = 192 # 缩略图尺寸
    img_h = 108
    line_max = 20 # 大图纵横数量
    row_max = 20
    dirName = 'D:/Wrapbuffer/bing壁纸' # 素材图片位置
    img_paths = add_imgPath(dirName)
    join_img(img_paths)