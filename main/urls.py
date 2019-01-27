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

    # /album/<id>
    url(r'^album/(?P<id>[0-9]+)/$', views.show_album, name='show_album'),

    # /album/<id>
    url(r'^artist/(?P<id>[0-9]+)/$', views.show_artist, name='show_artist'),

    # /song/<id>
    url(r'^song/(?P<id>[0-9]+)/$', views.show_song, name='show_song'),

    # /artists/
    url(r'^artists/$', views.all_artists, name='all_artists'),

    # /albums/
    url(r'^albums/$', views.all_albums, name='all_albums'),

    # /songs/
    url(r'^songs/$', views.all_songs, name='all_songs'),

    # /
    url(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
