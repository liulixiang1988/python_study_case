#!/usr/bin/env python
#-*- coding:utf-8 -*-
from faker import Factory
import requests
from PIL import Image
from io import BytesIO

url = 'http://www.tlnews.cn/toupiao/tlhr201405.asp'
image_url = 'http://www.tlnews.cn/toupiao/safecode/code8/code8_1.asp'
vote_url = 'http://www.tlnews.cn/toupiao/datasubmittlhr1405.asp'

vote_data = {'username': 'andrew',
             'user_tel': '18656212991',
             'user_id': '341202198805032317',
             'yzm': '',
             'Submit': '提交'}
faker = Factory.create(locale='zh_CN')

s = requests.Session()
r = s.get(url)
r2 = s.get(image_url)
img = Image.open(BytesIO(r2.content))
img.save('d:/1.jpg')
validate_code = input('请打开D盘，查看并输入1.jpg中的验证码:')
print('您输入的验证码是%s' % validate_code)
vote_data['yzm'] = validate_code


def vote():
    ip = faker.ipv4()
    headers = {'X-Forwarded-For': ip, 'CLIENT_IP': ip,
               'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'}
    try:
        for i in range(3):
            rp = s.post(vote_url, data=vote_data, headers=headers)
            print(rp.encoding)
            with open('d:/%d' % i, 'w+', encoding='utf-8') as f:
                f.write(rp.text)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    vote()