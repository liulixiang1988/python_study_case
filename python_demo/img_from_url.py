#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image
import requests
try:
    from cStringIO import StringIO #python 2
except ImportError:
    from io import BytesIO as StringIO #python 3

import pytesseract

url = 'http://tp.akxw.cn/vote/validcode.aspx?id=0139edf8-74f5-4c63-adcd-be9e94f64584'
response = requests.get(url)
i = StringIO(response.content)
img = Image.open(i)
img.save('a.gif')

print(pytesseract.image_to_string(img))
