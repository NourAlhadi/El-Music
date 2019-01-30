from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from elmusic import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'', include('main.urls'), name='index'),
    url(r'^_media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^_static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
