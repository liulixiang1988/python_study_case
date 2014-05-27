#!/user/bin/env python
# -*- coding:utf-8 -*-

import requests
import json

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 

url = 'http://365jia.cn/zt/qnwmh/doVote'
vote_data = {'id': '678998'}


def vote(proxy_addr):
    proxy = {'http': proxy_addr}
    try:
        print('start:', proxy_addr)
        r = requests.post(url, data=vote_data, proxies=proxy)
        print(proxyaddr, '\t', json.loads(r.text)['message'])
    except Exception:
        pass

with open('proxy.txt', 'r+', encoding='utf-8') as f:
    proxyaddrs = ['http://' + line.split('@', 1)[0] for line in f.readlines()]
    pool = ThreadPool(8)
    pool.map(vote, proxyaddrs)
    pool.close()
    pool.join()
