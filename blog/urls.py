from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<pk>\d+)-(?P<slug>[-\w]*)/$', views.profile, name='entry_detail'),
    url(r'^index/$', views.index),
    url(r'^register/$', views.register),
    url(r'^log_in/$', views.log_in),
]

