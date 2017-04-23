from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.test, name='test'),  
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.test, name='test'),
    url(r'^web/', views.test, name='test'),
    url(r'^new/', views.test, name='test'),
    url(r'^popular/', views.test, name='test'),
    url(r'^question/(\d+)/', views.test, name='test'),
]