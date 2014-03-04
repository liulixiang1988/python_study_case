__author__ = 'liulixiang'

from django.conf.urls import patterns, url
from auth import views

urlpatterns = patterns('',
                       url('^github-connect', views.github_connect, name='github_connect'),
                       url('^github-callback', views.github_callback, name='github_callback'),)
