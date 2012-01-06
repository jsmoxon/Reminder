from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', direct_to_template, {'template': 'home.html'}),
     url(r'^list/', 'reminders.views.list'),
     url(r'^log_view', 'reminders.views.log_view'),
     url(r'^logout_action', 'reminders.views.logout_action'),
     url(r'^send_reminder', 'reminders.views.send_a_reminder'),
     url(r'^reminders/', include('reminders.urls')),
)
