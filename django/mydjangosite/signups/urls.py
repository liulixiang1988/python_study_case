__author__ = 'liulixiang'

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='signup'),
                       url(r'^thank-you', views.thank_you, name='thank-you'),
                       )
