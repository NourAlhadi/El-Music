from django.shortcuts import render
from django.views.generic import ListView
from .models import *


def index(request):
    alb = Album.objects.all()
    art = Artist.objects.all()
    song = Song.objects.all()

    return render(request, 'main/index.html', {
        'albums': alb,
        'artist': art,
        'songs': song,
    })