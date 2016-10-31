
from django.conf.urls import url
from diary import views
urlpatterns = [
    url(r'^add/$', views.diary_add, name='diary_add'),
    url(r'^calendar/$', views.diary_calendar, name='diary_calendars'),

]
