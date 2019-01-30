from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [

    # /accounts/signup
    path('signup/', views.SignUp.as_view(), name='signup'),

    # /accounts/add/song
    url(r'^add/song/$', views.add_song, name='add_fav_song'),

    # /accounts/remove/song
    url(r'^remove/song/$', views.remove_song, name='remove_fav_song'),

    # /accounts/add/artist
    url(r'^add/artist/$', views.add_artist, name='add_fav_artist'),

    # /accounts/remove/artist
    url(r'^remove/artist/$', views.remove_artist, name='remove_fav_artist'),

    # /accounts/add/album
    url(r'^add/album/$', views.add_album, name='add_fav_album'),

    # /accounts/remove/album
    url(r'^remove/album/$', views.remove_album, name='remove_fav_album'),

    # /accounts/remove/album
    url(r'^remove/review/(?P<id>[0-9]+)/$', views.remove_review, name='remove_review'),

    # /accounts/my
    url(r'^my/$', views.show_profile, name='show_profile'),
]