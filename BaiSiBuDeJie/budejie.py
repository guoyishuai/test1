# -*- coding: utf-8 -*-
from urllib import request
import re

def getVidio(yema):
    url = "http://www.budejie.com/video/%s" %yema
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    req = request.Request(url, headers=headers)
    page = request.urlopen(req).read()
    page = page.decode('utf-8')

    mp4Re = r'http://.*wpd.mp4'
    mp4 = re.findall(mp4Re, page)
    print (mp4)
    for i in mp4:
        filename = i.split("/")[-1]
        print (url)
        print ("正在下载%s" %filename)
        request.urlretrieve(i,"D:\\1\\%s" %filename)

for i in range(1,5):
    getVidio(i)



