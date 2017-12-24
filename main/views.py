from django.shortcuts import render, redirect
from .models import *
from .forms import AlbumForm, ArtistForm, SongForm


def index(request):
    alb = Album.objects.all()
    art = Artist.objects.all()
    song = Song.objects.all()

    return render(request, 'main/index.html', {
        'albums': alb,
        'artist': art,
        'songs': song,
    })


def artist_form(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ArtistForm()
    return render(request, 'main/add.html', {
        'form': form,
        'to_add': 'Artist'
    })


def album_form(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AlbumForm()
    return render(request, 'main/add.html', {
        'form': form,
        'to_add': 'Album'
    })


def song_form(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SongForm()
    return render(request, 'main/add.html', {
        'form': form,
        'to_add': 'Song'
    })


def show_album(request, id):
    try:
        album = Album.objects.filter(id=id)
    except(Exception, BaseException):
        return render(request,'main/http404.html')

    if not album:
        return render(request,'main/http404.html')
    return render(request, 'main/details.html',{
        'album':album
    })


def show_artist(request, id):
    try:
        artist = Artist.objects.filter(id=id)
    except(Exception, BaseException):
        return render(request,'main/http404.html')

    if not artist:
        return render(request,'main/http404.html')
    return render(request, 'main/details.html',{
        'album':artist
    })

