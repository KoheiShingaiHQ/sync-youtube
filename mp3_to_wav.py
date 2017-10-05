# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
import sys
from pydub import AudioSegment

dir = os.path.dirname(os.path.realpath(__file__)) + '/storage/'

if (len(sys.argv) != 2):
    print 'Usage: $ python %s {YouTube Video ID}' % sys.argv[0]
    quit()
                
id = sys.argv[1]

sounds = AudioSegment.from_mp3(dir + id + '.mp3')
for i in range(len(sounds)/30000):
  rem = len(sounds) - i * 30000
  sound = sounds[-rem:]
  sound[:30000].export(dir + id + '.' + str(i) + '.wav', format='wav')
