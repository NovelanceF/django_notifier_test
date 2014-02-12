from django.conf.urls import patterns, url

from post import views

urlpatterns = patterns("",
                       url(r'^$', views.post_index, name='index'),
                       url(r'^adding/$', views.post_save, name='save'))
