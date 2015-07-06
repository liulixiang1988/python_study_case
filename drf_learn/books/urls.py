# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
__author__ = 'Liu Lixiang'

urlpatterns = [
    url('^books/all$', views.all_books, name='all_books'),
    url('^books/add$', views.add_book, name='add_book'),
    url('^books/author/add$', views.add_author, name='add_author'),
]
