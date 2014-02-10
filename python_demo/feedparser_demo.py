#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liulixiang'

import feedparser

d = feedparser.parse('http://www.reddit.com/r/python/.rss')
print(d['feed'])
print(d['feed']['title'])
print(d['feed']['link'])
print(d.feed.subtitle)
print(len(d.entries))
print(d.entries[0])

