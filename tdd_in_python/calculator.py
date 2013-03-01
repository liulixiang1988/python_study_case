#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Calculator(object):
    """A Simple Caculator"""
    def __init__(self):
        super(Calculator, self).__init__()
        
    def add(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError