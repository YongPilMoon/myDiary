from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^diary/', include('diary.urls', namespace='diary')),
    url(r'^admin/', admin.site.urls),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^index/$', TemplateView.as_view(template_name='index.html'), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
