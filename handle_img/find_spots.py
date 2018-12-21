# -*- encoding: utf-8 -*-
import os, time, cv2
import numpy as np


def box_nose(fpath, nose_cascade):
    # im = cv2.imread("photos/0.jpg", cv2.IMREAD_GRAYSCALE)
    image = cv2.imread(fpath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    info = image.shape
    x, y, h, w = 0, 0, info[0], info[1]
    roi_gray = gray[y:y+h, x:x+w]
    nose = nose_cascade.detectMultiScale(roi_gray, 1.3, 5)
    imgs = []
    for (nx, ny, nw, nh) in nose:
        if nw > 700 and nh > 500 and ny > 2200:
            if fpath.find('Left') > 0:
                imgs.append(image[int(round(ny-nh/3)):ny+nh, nx:int(round(nx+nw*3/2))]) # y0,y1,x0,x1
            elif fpath.find('Right') > 0:
                imgs.append(image[int(round(ny-nh/3)):ny+nh, int(round(nx-nw/2)):nx+nw])
            else:
                imgs.append(image[int(round(ny-nh/6)):int(round(ny+nh*3/4)), nx:nx+nw])
    return imgs[0]

def get_median(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2

def creat_params():
    params = cv2.SimpleBlobDetector_Params()
    params.minRepeatability = 2
    params.minDistBetweenBlobs = 8
    # params.thresholdStep = 10
    params.minThreshold = 5
    params.maxThreshold = 600

    params.filterByColor = True
    params.blobColor = 0

    params.filterByArea = True
    params.minArea = 8
    params.maxArea = 400

    params.filterByCircularity = True
    params.minCircularity = 0.2

    params.filterByInertia = True
    params.minInertiaRatio = 0.36

    params.filterByConvexity = True
    params.minConvexity = 0.3

    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)
    return detector
   
def main(path):
    nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
    nose_cascade.load('C:/Users/gang/Documents/Repository/opencv/data/haarcascades/haarcascade_mcs_nose.xml')
    detector = creat_params()
    fnames = os.listdir(path)
    output = open('results/result.txt', 'w')
    for num, fname in enumerate(fnames):
        im = box_nose('{}/{}'.format(path,fname), nose_cascade)
        cv2.imshow("Keypoints", im)
        keypoints = detector.detect(im)
        spots_count = len(keypoints)
        spots_size = []
        for point in keypoints:
            spots_size.append(point.size)
        s_mean, s_median, s_max, s_min = sum(spots_size)/spots_count, get_median(spots_size), max(spots_size), min(spots_size)
        vari = sum([(x-s_mean)**2 for x in spots_size])/(spots_count-1)
        area = im.shape[0]*im.shape[1]
        percent = sum(spots_size)/area
        output.write('>>>图:{}  '.format(fname)+'\n')
        output.write('黑头总数：{}\n平均值：{}\n方差：{}\n中位数：{}\n最大值：{}\n最小值：{}\n面积占比：{}\n'.format(spots_count, s_mean, vari, s_median, s_max, s_min, percent)+'\n\n')
        im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imwrite('results/{}'.format(fname), im_with_keypoints)
        # cv2.imshow("Keypoints", im_with_keypoints)
        # cv2.waitKey(0)
    print('请关闭窗口，查看结果！')
    print('>>>>>>Done!<<<<<<<')
    time.sleep(3)
    


if __name__ == '__main__':
    main('photos')