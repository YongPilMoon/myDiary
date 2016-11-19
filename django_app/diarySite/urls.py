from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^diary/', include('diary.urls', namespace='diary')),
    url(r'^admin/', admin.site.urls),
    url(r'^member/', include('member.urls', namespace='member')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )