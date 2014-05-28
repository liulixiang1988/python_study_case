__author__ = 'liulixiang'

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                url('^$', views.index, name='index'),
                url('^post/(?P<pk>\d+)\$', views.post, name='post'),
                )