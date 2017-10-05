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
    print ('Usage: $ python '+ sys.argv[0] +' {YouTube Video ID}')
    quit()
                
id = sys.argv[1]

i = 0
edges = []
while True:
  img = cv2.imread(in_dir + id + '.' + str(i) + '.png', 0)
  if img is None:
    break
  else:
    # edge = cv2.Canny(img,100,200)
    edge = img
    h, w = edge.shape
    edges.append(edge[0:h, 100:(w - 105)])
    # edges.append(edge[0:h, 0:w])
  i += 1

output = np.rot90(cv2.hconcat(edges))
cv2.imwrite(out_dir + id + '.edge.png', output,(5,5))