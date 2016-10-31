
from django.conf.urls import url
from diary import views
urlpatterns = [
    url(r'^add/$', views.diary_add, name='diary_add'),
    url(r'^calendar/$', views.diary_calendar, name='diary_calendars'),
    url(r'^calendar/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$',
        views.calendar_detail, name='calendar_detail'),
]
