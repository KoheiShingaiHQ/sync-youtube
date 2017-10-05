# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import os
import collections
import cv2
import csv

np.set_printoptions(threshold=np.nan)

in_dir = os.path.dirname(os.path.realpath(__file__)) + '/output/'
out_dir = os.path.dirname(os.path.realpath(__file__)) + '/storage/'

if (len(sys.argv) != 3):
    print ('Usage: $ python '+ sys.argv[0] +' {YouTube Video ID 1}  {YouTube Video ID 2}')
    quit()
    
def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image
    
def morph(img):
    kernel = np.ones((3, 3),np.uint8)
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
    return opened
                
id1 = sys.argv[1]
id2 = sys.argv[2]
img1 = cv2.imread(in_dir + id1 + '.edge.png', 0)
img2 = cv2.imread(in_dir + id2 + '.edge.png', 0)

ret1,thresh1 = cv2.threshold(img1,127,255,0)
ret2,thresh2 = cv2.threshold(img2,127,255,0)
imgEdge1,contours1,hierarchy1 = cv2.findContours(thresh1, 1, 2)
imgEdge2,contours2,hierarchy2 = cv2.findContours(thresh2, 1, 2)

cnt1 = contours1[0]
cnt2 = contours2[0]
M1 = cv2.moments(cnt1)
M2 = cv2.moments(cnt2)
cx1 = int(M1['m10']/M1['m00'])
cy1 = int(M1['m01']/M1['m00'])
area1 = cv2.contourArea(cnt1)
perimeter1 = cv2.arcLength(cnt1,True)
epsilon1 = 0.0001*cv2.arcLength(cnt1,True)
approx1 = cv2.approxPolyDP(cnt1,epsilon1,True)
cx2 = int(M2['m10']/M2['m00'])
cy2 = int(M2['m01']/M2['m00'])
area2 = cv2.contourArea(cnt2)
perimeter2 = cv2.arcLength(cnt2,True)
epsilon2 = 0.0001*cv2.arcLength(cnt2,True)
approx2 = cv2.approxPolyDP(cnt2,epsilon2,True)
print('img1 - (cx: ' + str(cx1) + ', cy: ' + str(cy1) + ', area: ' + str(area1) + ', perimeter: ' + str(perimeter1) + ')')
print('img2 - (cx: ' + str(cx2) + ', cy: ' + str(cy2) + ', area: ' + str(area2) + ', perimeter: ' + str(perimeter2) + ')')
#print("---- img1")
#print(approx1)
#print("---- img2")
#print(approx2)
h1 = img1.shape[0]
w1 = img1.shape[1]
h2 = img2.shape[0]
w2 = img2.shape[1]
img1 = cv2.imread(in_dir + id1 + '.edge.png')
img1 = create_blank(w1, h1)
img2 = cv2.imread(in_dir + id2 + '.edge.png')
img2 = create_blank(w2, h2)
cv2.circle(img1, (cx1, cy1), 5, (0, 0, 255), -1)
cv2.circle(img2, (cx2, cy2 + (cy1 - cy2)), 5, (0, 0, 255), -1)
#cv2.drawContours(img1, [cnt1], 0, (255,255,255), 3)
#cv2.drawContours(img2, [cnt2], 0, (255,255,255), 3)

csv1 = []
for i in approx1:
  cv2.circle(img1, (i[0][0], i[0][1]), 3, (255, 255, 0), -1)
  csv1.append([i[0][1], i[0][0]])

csv2 = []
for i in approx2:
  cv2.circle(img2, (i[0][0], i[0][1] + (cy1 - cy2)), 3, (255, 255, 0), -1)
  csv2.append([i[0][1], i[0][0]])
  
with open(out_dir + id1 + '.cnt.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['x','y'])
    writer.writerows(sorted(csv1))

with open(out_dir + id2 + '.cnt.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['x','y'])
    writer.writerows(sorted(csv2))

cv2.imwrite(out_dir + id1 + '.cnt.png', img1)
cv2.imwrite(out_dir + id2 + '.cnt.png', img2)