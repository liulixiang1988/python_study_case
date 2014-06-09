#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
from PIL import Image
from io import BytesIO
url = 'http://www.tlnews.cn/toupiao/tlhr201405.asp'
image_url = 'http://www.tlnews.cn/toupiao/safecode/code8/code8_1.asp'

s=requests.Session()
r = s.get(url)
r2 = s.get(image_url)
i = Image.open(BytesIO(r2.content))
i.save('d:/2.jpg')
