from django.shortcuts import render, redirect, render_to_response
from .models import *
from .forms import AlbumForm, ArtistForm, SongForm
from .utils import *


def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response


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
    album = Album.objects.filter(id=id)
    if len(album) == 0:
        return render(request,'error.html',{
            'error_title': 'Request Error',
            'error_body': 'You request contained an error: Album not found'
        })
    album = album[0]

    if request.method == "POST":
        fstars = request.POST.get("stars")
        freview = request.POST.get("review")
        fperson = request.POST.get("person")
        review = Review()
        review.stars = fstars
        review.body = freview
        review.album = album
        review.person = fperson
        print(review)
        review.save()
        return redirect('main:show_album', id=id)

    album = album

    all_reviews = 0
    stars = 0

    reviews = album.review_set
    for review in reviews.iterator():
        stars += review.stars
        all_reviews += 1

    stars /= max(all_reviews, 1)
    stars = round(stars)

    star_temp = ""
    for _ in range(stars):
        star_temp += "<span class=\"glyphicon glyphicon-star\"></span>"
    for _ in range(5 - stars):
        star_temp += "<span class=\"glyphicon glyphicon-star-empty\"></span>"

    return render(request, 'main/show_albums.html', {
        'album': album,
        'stars': stars,
        'star_temp': star_temp
    })


def show_artist(request, id):
    artist = Artist.objects.filter(id=id)
    if len(artist) == 0:
        return render(request,'error.html',{
            'error_title': 'Request Error',
            'error_body': 'You request contained an error: Review not found'
        })
    artist = artist[0]

    if request.method == "POST":
        fstars = request.POST.get("stars")
        freview = request.POST.get("review")
        fperson = request.POST.get("person")
        review = Review()
        review.stars = fstars
        review.body = freview
        review.artist = artist
        review.person = fperson
        review.save()
        return redirect('main:show_artist', id=id)

    artist = artist

    all_reviews = 0
    stars = 0

    reviews = artist.review_set
    for review in reviews.iterator():
        stars += review.stars
        all_reviews += 1

    stars /= max(all_reviews, 1)
    stars = round(stars)

    star_temp = ""
    for _ in range(stars):
        star_temp += "<span class=\"glyphicon glyphicon-star\"></span>"
    for _ in range(5 - stars):
        star_temp += "<span class=\"glyphicon glyphicon-star-empty\"></span>"

    return render(request, 'main/show_artists.html', {
        'artist': artist,
        'stars': stars,
        'star_temp': star_temp
    })


def show_song(request, id):
    song = Song.objects.filter(id=id)
    if len(song) == 0:
        return render(request,'error.html',{
            'error_title': 'Request Error',
            'error_body': 'You request contained an error: Song not found'
        })
    song = song[0]

    if request.method == "POST":
        fstars = request.POST.get("stars")
        freview = request.POST.get("review")
        fperson = request.POST.get("person")
        review = Review()
        review.stars = fstars
        review.body = freview
        review.song = song
        review.person = fperson
        review.save()
        return redirect('main:show_song', id=id)

    song = song

    all_reviews = 0
    stars = 0

    reviews = song.review_set
    for review in reviews.iterator():
        stars += review.stars
        all_reviews += 1

    stars /= max(all_reviews, 1)
    stars = round(stars)

    star_temp = ""
    for _ in range(stars):
        star_temp += "<span class=\"glyphicon glyphicon-star\"></span>"
    for _ in range(5 - stars):
        star_temp += "<span class=\"glyphicon glyphicon-star-empty\"></span>"

    return render(request, 'main/show_song.html', {
        'song': song,
        'stars': stars,
        'star_temp': star_temp
    })


def all_artists(request):
    artists = Artist.objects.all()
    criteria = 'stars'
    if request.GET.get('sort') != 'none':
        criteria = request.GET.get('sort')

    if criteria == 'stars':
        artists = sorted(artists, key=lambda a: stars(a.review_set))
    elif criteria == 'rates':
        artists = sorted(artists, key=lambda a: rates(a.review_set))
    elif criteria == 'name':
        artists = sorted(artists, key=lambda a: name(a.name))

    return render(request, 'main/artists.html', {
        'artists': artists
    })


def all_albums(request):
    albums = Album.objects.all()
    criteria = 'stars'
    if request.GET.get('sort') != 'none':
        criteria = request.GET.get('sort')

    if criteria == 'stars':
        albums = sorted(albums, key=lambda a: stars(a.review_set))
    elif criteria == 'rates':
        albums = sorted(albums, key=lambda a: rates(a.review_set))
    elif criteria == 'name':
        albums = sorted(albums, key=lambda a: name(a.title))

    return render(request, 'main/albums.html', {
        'albums': albums
    })


def all_songs(request):
    songs = Song.objects.all()
    criteria = 'stars'
    if request.GET.get('sort') != 'none':
        criteria = request.GET.get('sort')

    if criteria == 'stars':
        songs = sorted(songs, key=lambda a: stars(a.review_set))
    elif criteria == 'rates':
        songs = sorted(songs, key=lambda a: rates(a.review_set))
    elif criteria == 'name':
        songs = sorted(songs, key=lambda a: name(a.title))

    return render(request, 'main/songs.html', {
        'songs': songs
    })
