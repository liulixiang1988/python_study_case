# -*- coding: utf-8 -*-
"""
0 day down script
"""

import requests

#设置请求头信息
headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           }
           
s = requests.Session()
s.headers.update(headers)

print(s.get("http://www.odaydown.com/wp-login.php").text)

print('------------')

r = s.post("http://www.odaydown.com/wp-login.php", 
       {'log': 'liulixiang1988',
        'pwd': 'liulx123',
        'wp-submit':'登录',
        'redirect_to': 'http://www.odaydown.com/wp-admin/',
        'testcookie': 1})
        
print(r.text)