#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liulixiang'

import time

from functools import wraps


def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("%s - %d" % (func.__name__, end-start))
        return result
    return wrapper


@time_this
def count(n):
    while n > 0:
        n -= 1

count(100000000)


