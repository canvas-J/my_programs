# -*- encoding=utf-8 -*-
import os, random, time, numpy, numexpr
from PIL import Image, ImageFont, ImageDraw


def transfer(img_path, dst_width, dst_height):
    im = Image.open(img_path)
    if im.mode != "RGBA":
        im = im.convert("RGBA")
    tmp_img = im.resize((dst_width, dst_height))
    return numpy.array(tmp_img)[:dst_height, :dst_width]

def add_path():
    img_paths = []
    src = os.getcwd()+"/photos/"
    for na in os.listdir(src):
	    if os.path.splitext(na)[-1] == ".jpg":
		    img_paths.append(src + na)
    return img_paths

def createImg():
    img_paths = add_path()
    iW_size = W_num * W_size
    iH_size = H_num * H_size
    I = numpy.array(transfer("base.jpg", iW_size, iH_size))
    I = numexpr.evaluate("""I*(1-alpha)""")
    for i in range(W_num):
	    for j in range(H_num):
		    SH = I[(j*H_size):((j+1)*H_size), (i*W_size):((i+1)*W_size)]
		    DA = transfer(random.choice(img_paths), W_size, H_size)
		    results  = numexpr.evaluate("""SH+DA*alpha""")
		    I[(j*H_size):((j+1)*H_size), (i*W_size):((i+1)*W_size)] = results
    big_img = Image.fromarray(I.astype(numpy.uint8))
    return big_img.rotate(359, expand=10)

def writeToImage(big_img):
    print("正在向图片中添加祝福语...")
    font = ImageFont.truetype('C:/Windows/Fonts/Lobster-Regular.ttf', 60)
    draw = ImageDraw.Draw(big_img, mode='RGBA')
    draw.text((W_size * 0.5, H_size * H_num), "happy life written by python", (14, 190, 68), font=font)
    big_img.save("final_%s.png" % alpha)

if __name__ == "__main__":
    STAG = time.time()
    W_num = 10
    H_num = 10
    W_size = 192
    H_size = 108
    alpha = 0.5
    writeToImage(createImg())
    print("Total Time %s"%(time.time()-STAG))