# -- coding: utf-8 --

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^new/', views.test, name='test'),
    url(r'^popular/', views.popular, name='popular'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.question, name='question'),
]