#!/user/bin/env python
# -*- coding:utf-8 -*-

import requests
import requests.exceptions
from faker import Factory
import json

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 

url = 'http://365jia.cn/zt/qnwmh/doVote'
vote_data = {'id': '678998'}
faker = Factory.create(locale='zh_CN')

def vote(proxy_addr):
    proxy = {'http': proxy_addr}
    ip = faker.ipv4()
    headers = {'X-Forwarded-For': ip, 'CLIENT_IP': ip}
    try:
        print('start:', proxy_addr)
        r = requests.post(url, data=vote_data, proxies=proxy, headers=headers)
        if r.status_code == requests.codes.ok:
            print(proxy_addr, '\t', r.text)
        else:
            print(proxy_addr, '该地址已经被禁用', r.text)
    except TimeoutError as e:
        print(e)
    except requests.exceptions.ProxyError as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)

with open('proxy.txt', 'r+', encoding='utf-8') as f:
    proxyaddrs = ['http://' + line.split('@', 1)[0] for line in f.readlines()]
    pool = ThreadPool(8)
    pool.map(vote, proxyaddrs)
    pool.close()
    pool.join()