# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import os
import collections
import cv2

np.set_printoptions(threshold=np.nan)

in_dir = os.path.dirname(os.path.realpath(__file__)) + '/storage/'
out_dir = os.path.dirname(os.path.realpath(__file__)) + '/output/'

if (len(sys.argv) != 2):
    print ('Usage: $ python '+ sys.argv[0] +' {URL hash}')
    quit()
                
hash = sys.argv[1]

img1 = cv2.imread(in_dir + hash + '.desktop.png', 0)
edge1 = cv2.Canny(img1,100,200)

img2 = cv2.imread(in_dir + hash + '.mobile.png', 0)
edge2 = cv2.Canny(img2,100,200)

ret1,thresh1 = cv2.threshold(img1,127,255,0)
ret2,thresh2 = cv2.threshold(img2,127,255,0)
imgEdge1,contours1,hierarchy1 = cv2.findContours(thresh1, 1, 2)
imgEdge2,contours2,hierarchy2 = cv2.findContours(thresh2, 1, 2)

cnt1 = contours1[0]
cnt2 = contours2[0]

cv2.drawContours(edge1, [cnt1], 0, (255,255,255), 3)
cv2.drawContours(edge2, [cnt2], 0, (255,255,255), 3)

cv2.imwrite(in_dir + hash + '.desktop.png', edge1)
cv2.imwrite(in_dir + hash + '.mobile.png', edge2)