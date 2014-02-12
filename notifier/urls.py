from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'notifier.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/', include('post.urls', namespace='post')),
)
