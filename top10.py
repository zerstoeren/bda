#!/usr/bin/env python

import os
import json

gen10 = os.system('tshark -r airportSniffcQjzMD.cap -Y http.request -T fields -e http.host -e http.request.uri|sed -e \'s/?.*$//\'|sed -e \'s#^\(.*\)\t\(.*\)$#http://\1\2#\'|sort | uniq -c | sort -rn | head')

with open('json.txt', 'w') as outfile:
	json.dump(gen10, outfile, sort_keys = True, indent = 4, ensure_ascii=False)

