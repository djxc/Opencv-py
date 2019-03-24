# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:48:22 2019

@author dj
"""
import OperateImg as djimg
import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")       # 添加参数简写、全称、必须或可选、参数的介绍
args = vars(ap.parse_args())

img = cv2.imread(args["image"])                                                 # 第二个参数1为彩色图像模式， 0为灰色图像模式
#OperateImg.showImg(OperateImg.moveImg(img, 200, 150))
#djimg.showImg(djimg.rotationImg(img, 180))
#djimg.showImg(djimg.resizeImg(img, 5, 5))
#djimg.showImg(cv2.flip(img, 1))                                                 # 反转；1以y轴为对称轴；0以x轴为对称轴；-1以x与y为对称轴
#djimg.showImg(img[50:120, 250:320])                                            # 截取图片的一部分,y在前，x在后    
#djimg.showImg(djimg.changeValue(img, -50))

djimg.showImg(djimg.circleMask(img, (250, 100), 80))