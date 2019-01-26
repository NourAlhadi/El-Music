from django.shortcuts import render, redirect
from .models import *
from .forms import AlbumForm, ArtistForm, SongForm


def index(request):
    alb = Album.objects.all()
    art = Artist.objects.all()
    song = Song.objects.all()

    return render(request, 'main/index.html', {
        'albums': alb,
        'artists': art,
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
    album = album[0]
    return render(request, 'main/show_albums.html', {
        'album': album
    })


def show_artist(request, id):
    try:
        artist = Artist.objects.filter(id=id)
    except(Exception, BaseException):
        return render(request,'main/http404.html')

    if not artist:
        return render(request,'main/http404.html')

    if request.method == "POST":
        fstars = request.POST.get("stars")
        freview = request.POST.get("review")
        fperson = request.POST.get("person")
        review = Review()
        review.stars = fstars
        review.body = freview
        review.artist = artist[0]
        review.person = fperson
        review.save()

    artist = artist[0]

    all_reviews = 0
    stars = 0

    reviews = artist.review_set
    for review in reviews.iterator():
        stars += review.stars
        all_reviews += 1

    stars /= max(all_reviews,1)
    stars = round(stars)

    star_temp = ""
    for _ in range(stars):
        star_temp += "<span class=\"glyphicon glyphicon-star\"></span>"
    for _ in range(5 - stars):
        star_temp += "<span class=\"glyphicon glyphicon-star-empty\"></span>"

    return render(request, 'main/show_artists.html',{
        'artist': artist,
        'stars': stars,
        'star_temp': star_temp
    })

