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
    print ('Usage: $ python '+ sys.argv[0] +' {URL Hash}')
    quit()

id = sys.argv[1]

img1 = cv2.imread(in_dir + id + '.desktop.png')
img2 = cv2.imread(in_dir + id + '.mobile.png')

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

good = []
mean = 0
count = 0
for m,n in matches:
    #print(str(m.distance) + ' - ' + str(n.distance))
    mean += m.distance
    count += 1
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)

cv2.imwrite(out_dir + id + '.diff.png', img3)