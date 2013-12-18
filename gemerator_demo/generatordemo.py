#-*- coding:utf-8 -*-
#/usr/bin/env python

import random

def get_data():
    '''返回0-9，3个数字'''
    return random.sample(range(10), 3)

def consume():
    '''显示传入列表的动态平均值'''
    running_sum = 0
    data_itmes_seen = 0
    while True:
        data = yield
        data_itmes_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_itmes_seen)))

def produce(consumer):
    '''产生序列集合，传给消费者'''
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield

if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print('Producing')
        next(producer)
