# -*- coding: UTF-8 -*-
from scipy.signal import argrelmax
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import os
import collections

np.set_printoptions(threshold=np.nan)
plt.rcParams['agg.path.chunksize'] = 20000

dir = os.path.dirname(os.path.realpath(__file__)) + '/storage/'

if (len(sys.argv) != 2):
    print 'Usage: $ python %s {YouTube Video ID}' % sys.argv[0]
    quit()
                
id = sys.argv[1]

i = 0
while True:
  wr = wave.open(dir + id + '.' + str(i) + '.wav', 'r')
  if wr is None:
    break
  else:
    signal = wr.readframes(wr.getframerate()*30)
    signal = np.fromstring(signal, 'Int16')
    signal = signal
    plt.figure(1)
    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    plt.axis([0, 3000000 - (48000 - wr.getframerate())*62, -40000, 40000])
    plt.plot(signal, color='W')
    plt.savefig(dir + id + '.' + str(i) + '.png')
  i += 1