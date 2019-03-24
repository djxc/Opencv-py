# -*- coding: utf-8 -*-
import cv2
import numpy as np
import OperateImg as djimg

print("max {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))

rectangle = np.ones((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)

circle = np.ones((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
bitwiseOr = cv2.bitwise_or(rectangle, circle)
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
bitwiseNot = cv2.bitwise_not(rectangle)

djimg.showImg(bitwiseAnd)
img = cv2.imread("data/wave.png")
(B, G, R) = cv2.split(img)
djimg.showImg(R)
