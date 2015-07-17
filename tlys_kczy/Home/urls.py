from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^introduction/$', views.introduction,
                           name='intro'),
                       url(r'^datas/$', views.datas, name='datas'),
                       url(r'^data/(?P<article_id>\d+)/$',
                           views.data, name="data"),
                       url(r'^literatures/$',
                           views.literatures, name='literatures'),
                       url(r'^literature/(?P<article_id>\d+)/$',
                           views.literature, name="literature"),
                       url(r'^images/$',
                           views.images, name='images'),
                       url(r'^image/(?P<article_id>\d+)/$',
                           views.image, name="image"),
                       url(r'^videos/$',
                           views.videos, name='videos'),
                       url(r'^video/(?P<article_id>\d+)/$',
                           views.video, name="video"),)
