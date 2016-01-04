#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

def main():
	print(__file__)
	print(os.path.dirname(__file__))
	path = os.path.abspath(__file__)
	print(os.path.dirname(os.path.dirname(__file__)))
	print(sys.path)
	sys.path.append(os.path.dirname(os.path.dirname(path)))
	print(sys.path)
	print(os.path.dirname('..'))

if __name__ == '__main__':
	main()
