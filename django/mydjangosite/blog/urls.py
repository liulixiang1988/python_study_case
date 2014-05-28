__author__ = 'liulixiang'

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
                url(r'^category/(?P<pk>\d+)/$', views.category, name='category')
                )