from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [

    # /add/song
    url(r'^add/artist/$', views.artist_form, name='add_artist'),

    # /add/song
    url(r'^add/album/$', views.album_form, name='add_album'),

    # /add/song
    url(r'^add/song/$', views.song_form, name='add_song'),

    # /
    url(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
