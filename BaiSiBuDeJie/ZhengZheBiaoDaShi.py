# -*- coding: UTF-8 -*-
import re

# line = 'cars are smater than dog'
# matchObj = re.match(r'(.*)are(.*?).*',line)
# if matchObj:
#     print (matchObj.group())
#     print (matchObj.group(1))
#     print (matchObj.group(2))
# else:
#     print ("no match")
#
# matchObj = re.search(r'(cars.*than|.dog)', line)
# if matchObj:
#     print (matchObj.group())
#     print (matchObj.group(4))
#
# else:
#     print ("no match")


key = r"123<h1>hello world<h1>123"
p1 = r"<h1>.*<h1>"
print (key)
print (re.findall(p1, key))

