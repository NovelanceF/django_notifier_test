from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'notifier.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/', include('post.urls', namespace='post')),
    url(r'^accounts/login/$', 'notifier.views.login_view', name='notifierin'),
    url(r'^accounts/logout/$', 'notifier.views.logout_view', name='notifier'),
    url(r'^accounts/relog/$', 'notifier.views.re_log', name='relog'),
)
