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

in_dir = os.path.dirname(os.path.realpath(__file__)) + '/storage/'
out_dir = os.path.dirname(os.path.realpath(__file__)) + '/output/'

if (len(sys.argv) != 2):
    print ('Usage: $ python '+ sys.argv[0] +' {YouTube Video ID}')
    quit()
                
id = sys.argv[1]
img = cv2.imread(out_dir + id + '.edge.png')

data = csv.reader(open(in_dir + id + '.peak.csv', 'r'))
header = next(data)

h = img.shape[0]
w = img.shape[1]

for line in data:
    peak = list(map(int, line))
    cv2.line(img, (0, peak[0]), (w, peak[0]), (0, 255, 255), 3)

cv2.imwrite(out_dir + id + '.peak.png', img)