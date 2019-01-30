from django.contrib.auth.models import AbstractUser
from main.models import *
from django import template

register = template.Library()


class ElmusicUser(AbstractUser):
    fav_albums = models.ManyToManyField(Album)
    fav_artists = models.ManyToManyField(Artist)
    fav_songs = models.ManyToManyField(Song)


    def __str__(self):
        return self.username

