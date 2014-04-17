# -*- coding:utf-8 -*-
__author__ = 'liulixiang'

import os


def populate():
    python_cat = add_catogory('Python')

    add_page(python_cat,
             title='Python4cn',
             url='http://simple-is-better.com/')

    add_page(python_cat,
             title='Python China',
             url='http://pychina.org/')

    add_page(python_cat,
             title='Python学习平台',
             url='http://www.pythoner.cn/')

    django_cat = add_catogory('Django')

    add_page(django_cat,
             title='Django Project',
             url='https://www.djangoproject.com/')

    add_page(django_cat,
             title='Django China',
             url='http://django-china.cn/')

    add_page(django_cat,
             title='GoDjango',
             url='https://godjango.com/')

    add_page(django_cat,
             title='Tango with Django',
             url='http://www.tangowithdjango.com/')

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p


def add_catogory(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

if __name__ == '__main__':
    print('Starting Rango populate script...')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydjangosite.settings')
    from rango.models import Category, Page
    populate()