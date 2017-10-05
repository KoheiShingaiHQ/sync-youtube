# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import sys
import youtube_dl

if (len(sys.argv) != 2):
    print 'Usage: $ python %s {YouTube Video ID}' % sys.argv[0]
    quit()
    
id = sys.argv[1]

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl' : unicode('./storage/' + '%(id)s.%(ext)s')
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=' + id])
