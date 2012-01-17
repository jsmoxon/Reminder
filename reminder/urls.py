from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.views.generic.simple import direct_to_template
from cloudmailin.views import MailHandler

urlpatterns = patterns('',
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', direct_to_template, {'template': 'landing.html'}),
     url(r'^landing', direct_to_template, {'template': 'landing.html'}),
     url(r'^list/', 'reminders.views.list'),
     url(r'^log_view', 'reminders.views.log_view'),
     url(r'^logout_action', 'reminders.views.logout_action'),
     url(r'^send_reminder', 'reminders.views.send_a_reminder'),
     url(r'^reminders/', include('reminders.urls')),
     url(r'^accounts/', include('registration.urls')),
)

mail_handler = MailHandler()
mail_handler.register_address(
    address='14af7a6e3133f0079033@cloudmailin.net'
    secret='mysupersecretkey',
    callback=my_callback_function
)

urlpatterns += patterns('',
     url(r'^cloudmailin/$', mail_handler)



urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
