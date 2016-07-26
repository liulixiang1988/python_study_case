#!usr/bin/env python
# -*- coding:utf-8 -*-

import sample

print('gcd:', sample.gcd(35, 42))
print('in_mandel:', sample.in_mandel(0, 0, 500))
print('in_mandel:', sample.in_mandel(2.0, 1.0, 500))
print('divide:', sample.divide(42, 8))
print('avg:', sample.avg([1, 2, 3]))

p1 = sample.Point(1, 2)
p2 = sample.Point(4, 5)
print('distance:', sample.distance(p1, p2))