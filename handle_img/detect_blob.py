# -*- encoding: utf-8 -*-
import cv2
import numpy as np


# 读取图像
# im = cv2.imread("photos/0.jpg", cv2.IMREAD_GRAYSCALE)
im = cv2.imread("photos/1.jpg")
im = im[2776:3708, 288:1624] # y0,y1,x0,x1
# 设置简单的斑点监测参数
params = cv2.SimpleBlobDetector_Params()
# 斑点距离、重复情况
params.minRepeatability = 2
params.minDistBetweenBlobs = 8
# 设置阈值大小
# params.thresholdStep = 10
params.minThreshold = 5
params.maxThreshold = 600
# 按颜色过滤
params.filterByColor = True
params.blobColor = 0
# 按面积过滤（基于像素单位的面积）
params.filterByArea = True
params.minArea = 9
params.maxArea = 600
# 按圆度过滤（0.75-0.8为矩形正多边形），越大越圆
params.filterByCircularity = True
params.minCircularity = 0.2
# 按惯性过滤，越大越圆
params.filterByInertia = True
params.minInertiaRatio = 0.36
# 按凸度过滤，越大越圆
params.filterByConvexity = True
params.minConvexity = 0.3
# 用以上参数创建滤波器
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)
# 检测斑点
keypoints = detector.detect(im)
# 用红色圆圈圈出斑点
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS 
# 确保圆的大小对应斑点大小
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# 显示斑点
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
