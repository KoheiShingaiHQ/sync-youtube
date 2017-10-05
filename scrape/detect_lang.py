# -*- coding: UTF-8 -*-
import sys
import os
import json
from langdetect import detect

dir = os.path.dirname(os.path.realpath(__file__)) + '/storage/'

if (len(sys.argv) != 2):
    print ('Usage: $ python '+ sys.argv[0] +' {Hash}')
    quit()
                
hash = sys.argv[1]

with open(dir + hash + '.json', 'r') as datas:
    data = json.load(datas)
    content = data['content']
    datas.close()

with open(dir + hash + '.json', 'w') as datas:
    data["lang"] = detect(content)
    json.dump(data, datas)
