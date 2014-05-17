from django.conf.urls import patterns, url

from led import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^on/(?P<led_id>\d+)$', views.detail, name='detail'),
    url(r'^off/(?P<led_id>\d+)$',views.detailoff,name='detailoff')
)

