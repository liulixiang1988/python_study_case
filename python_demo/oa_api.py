#!/user/bin/env python
# -*- coding:utf-8 -*-

import os
from bs4 import BeautifulSoup
import requests

# 从环境变量中读取配置
url = os.environ.get('oa_url', 'http://localhost:8080')
username = os.environ.get('oa_userid', 'test')
password = os.environ.get('oa_password', '123456')

# 设置请求头信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
    #"Referer":"http://www.tnmg.com.cn/Portal/UserLogin.aspx?ReturnUrl=%2fPortal%2fDefault.aspx",
    "Referer": url,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# 使用会话
s = requests.Session()

# 发送请求
r = s.get(url)

# 提取返回中的数据
soup = BeautifulSoup(r.text)
viewstate = soup.select('#__VIEWSTATE')[0].attrs['value']
validation = soup.select('#__EVENTVALIDATION')[0].attrs['value']
txtUserId = username
txtPassword = password
rbLoginType = 'on'
txtPin = ''
btnLogin = '登录'

# post参数
data = {
    '__VIEWSTATE': viewstate,
    '__EVENTVALIDATION': validation,
    'txtUserID': txtUserId,
    'txtPassword': txtPassword,
    'rbLoginType': rbLoginType,
    'txtPin': txtPin,
    'btnLogin': btnLogin
}

# 更新头信息
s.headers.update(headers)

# 发送登录的post请求，判断数据是否正确
r2 = s.post(url, data)
if r2.status_code == 200:
    print(r2.text)
else:
    print(r2.status_code)
