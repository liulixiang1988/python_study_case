__author__ = 'liulixiang'

from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='result'),
                       url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote')
)