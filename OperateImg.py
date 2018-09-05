# -*- coding: utf-8 -*-
import cv2
import numpy as np

"""获取图像相关的属性"""
def aboutImg(img):
    px = img[100, 10]
    print(px)
    print(img.shape)
    print(img.size)

"""修改图像的大小"""
def resizeImg():
    img = cv2.imread('data/demo1.jpg')   
    aboutImg(img)
    #OR
    height, width = img.shape[:2]
    res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
    aboutImg(res)
    showImg(res)

"""显示图像"""
def showImg(img):
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)     # 可以调整窗口大小
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    
"""对图像的移动，主要由M矩阵控制移动的方向和范围
第一维的第三个数控制左右平移大小;第二维第三个数控制上下平移大小"""
def moveImg(img):
    rows,cols = img.shape
    
    M = np.float32([[1,0,100],[0,1,50]])
    
    dst = cv2.warpAffine(img,M,(cols,rows))
    showImg(dst)
    
"""图像的旋转，第一个参数是旋转的中心，第二个是旋转的角度"""
def rotationImg(img):
    rows,cols = img.shape
    
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))    
    showImg(dst)
    
if __name__ == "__main__":
    img = cv2.imread('data/demo1.jpg')   
#    resizeImg()    
#    moveImg()
    rotationImg(img)    
