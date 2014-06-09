# !/user/bin/env python
# -*- coding:utf-8 -*-

import requests
import requests.exceptions
from faker import Factory
import json
from multiprocessing.dummy import Pool as ThreadPool

url = 'http://365jia.cn/zt/qnwmh/doVote'
vote_data = {'id': '678998'}
faker = Factory.create(locale='zh_CN')
print(url)


def vote(proxy_addr):
    proxy = {'http': proxy_addr}
    ip = faker.ipv4()
    headers = {'X-Forwarded-For': ip, 'CLIENT_IP': ip,
               'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'}
    try:
        r = requests.post(url, data=vote_data, proxies=proxy, headers=headers)
        if r.status_code == requests.codes.ok:
            print(proxy_addr, '\t', json.loads(r.text)['message'])
        else:
            print(proxy_addr, 'Error Message:', r.text)
    except Exception as e:
        pass


def main():
    while True:
        with open('proxy.txt', 'r+', encoding='utf-8') as f:
            proxyaddrs = ['http://' + line.split('@', 1)[0] for line in f.readlines()]
            try:
                pool = ThreadPool(8)
                pool.map(vote, proxyaddrs)
                pool.close()
                pool.join()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
