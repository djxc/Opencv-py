# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:48:22 2019

@author: gis
"""

import cv2
import numpy as np


def aboutImg(img):
    """获取图像相关的属性"""
    px = img[100, 10]
    print(px)
    print(img.shape)
    print(img.size)


def resizeImg(img, rw, rh):
    """修改图像的大小"""
    height, width = img.shape[:2]
    resized = cv2.resize(img,(int(rw*width), int(rh*height)),
                     interpolation = cv2.INTER_AREA)
    return resized
    

def showImg(img):
    """显示图像"""
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)     # 可以调整窗口大小
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    

def moveImg(img, x, y):
    """对图像的移动，主要由M矩阵控制移动的方向和范围
    第一维的第三个数控制左右平移大小;第二维第三个数控制上下平移大小"""
    M = np.float32([[1,0, x],[0,1, y]])                                        # M为转换矩阵
    shifted = cv2.warpAffine(img,M, (img.shape[1], img.shape[0]))              # 第一个参数为需要转换的图片‘第二个参数为转换矩阵；第三个参数为图片转换的维度
    return shifted
    

def rotationImg(img, angle, center = None, scale = 1.0):
    """图像的旋转，第一个参数是旋转的中心，第二个是旋转的角度"""
    rows,cols = img.shape[:2]
    if center is None:
        center = (cols/2, rows/2)    
    M = cv2.getRotationMatrix2D(center, angle, scale)                          # 旋转矩阵 
    rotated = cv2.warpAffine(img,M,(cols,rows))    
    return rotated

def changeValue(img, value):
    """图像改变值：首先创建一个和图像相同维度的矩阵，利用cv2里的函数进行相加或相减。输入的值必须为整数"""
    if value < 0:
        M = np.ones(img.shape, dtype="uint8") * (-value)
        return cv2.subtract(img, M)
    else:
        M = np.ones(img.shape, dtype="uint8") * value
        return cv2.add(img, M)


def circleMask(img, centerPoint, radius):
    """mask图片，首先构建一个圆形的图形，利用and计算"""
    mask = np.zeros(img.shape[:2], dtype="uint8")
    cv2.circle(mask, centerPoint, radius, 255, -1)
    return cv2.bitwise_and(img, img, mask=mask)
    


if __name__ == "__main__":
    img = cv2.imread('data/demo1.jpg')   
#    resizeImg()
    shifted = moveImg(img, 200, 180)
#    rotationImg(img)    
    showImg(shifted)