from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^introduction/$', views.introduction,
                           name='intro'),
                       url(r'^datas/$', views.datas, name='datas'),
                       url(r'^data/(?P<article_id>\d+)/$',
                          views.data, name="data"))
