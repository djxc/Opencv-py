# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

def readImg():        
    """读取图片，显示图片"""
    img = cv2.imread('data/demo1.jpg', -1)   # 第二个参数1为彩色图像模式， 0为灰色图像模式， -1
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)     # 可以调整窗口大小
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def saveImg(img):
    """保存图片"""
    cv2.imwrite('data/test.png', img)
    
def showImgbyMatplot(img):
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

if __name__ == "__main__":
    img = cv2.imread('data/trex.png', 1)
#    readImg()
#    saveImg(img)
    showImgbyMatplot(img)