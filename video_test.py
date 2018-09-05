# -*- coding: utf-8 -*-
import numpy as np
import cv2

"""获取摄像头的一帧图像
1、实例化一个视频捕获器
2、读取内容
3、转换为灰色图片并显示"""
def getCamera():
    cap = cv2.VideoCapture(0)
    print(cap.isOpened())
    cap.open(0)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
    
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(0):
            break
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
"""图像跟踪，通过摄像头获取的图像，转换为hsv样式，然后定义目标的颜色范围
通过二值分析获取对象轮廓样式"""
def ObjectTracking():
    cap = cv2.VideoCapture(0)
    while(1):
    
        # Take each frame
        _, frame = cap.read()
    
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
    
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)
    
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
          break
    cv2.destroyAllWindows()

"""播放视频"""
def playVideo():
    cap = cv2.VideoCapture('data/video.avi')

    while(cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()    

if __name__ == "__main__":
#    getCamera()
#    playVideo()
    ObjectTracking()
    