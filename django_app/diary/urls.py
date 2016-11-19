
from django.conf.urls import url
from diary import views
urlpatterns = [
    url(r'^add/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.diary_add, name='diary_add'),
    url(r'^calendar/month/$', views.month_calendar, name='month_calendar'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$',
        views.diary_detail, name='diary_detail'),
    url(r'^photo$', views.photo, name='photo'),

]
