__author__ = 'liulixiang'

from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
                       url(r'^add_category/$', views.add_category, name='add_category'),
                       url(r'^category/(?P<category_name_url>\w+)/add_page/$', views.add_page, name='add_page'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^profile/$', views.profile, name='profile'),
                       url(r'^track_url/(?P<page_id>\d+)/$', views.track_url, name='track_url'),
                       url(r'^like_category/$', views.like_category, name='like_category'),)
