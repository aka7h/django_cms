from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^register$','details.views.index', name='index'),
    url(r'^new$', 'details.views.user', name='user'),
    
    url(r'^admin/', include(admin.site.urls)),
)
