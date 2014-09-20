#!/usr/bin/env python

# -*- coding:uft-8 -*-

__author__ = 'liulixiang'


class Decorator:
    def __init__(self, f):
        print("inside decorator.__init__")
        self.f = f

    def __call__(self, *args, **kwargs):
        print("inside decorator.__call__")
        result = self.f(*args, **kwargs)
        print("finish decorator.__call__")
        return result


@Decorator
def function(*args):
    print("inside function", *args)


print("finish decorating function()")

function()