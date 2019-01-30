from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import CustomUserCreationForm
from accounts.models import ElmusicUser
from main.models import Song, Artist, Album, Review


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('main:login')
    template_name = 'registration/signup.html'


def add_song(request):
    if not request.is_ajax():
        return render(request, 'error.html', {
            'error_title': 'Only Ajax is allowed here',
            'error_body': 'For some reason you managed to access this route <br /> but we\'re sorry to inform you '
                          'that this route accepts only ajax requests '
        })
    user_id = request.GET.get('user_id')
    song_id = request.GET.get('song_id')

    user = ElmusicUser.objects.filter(pk=user_id)
    if len(user) == 0:
        data = {
            'added': False,
            'message': 'Invalid User',
        }
        return JsonResponse(data)
    user = user[0]
    song = Song.objects.filter(pk=song_id)
    if len(song) == 0:
        data = {
            'added': False,
            'message': 'Invalid Song',
        }
        return JsonResponse(data)
    song = song[0]
    already_fav = False
    if user.fav_songs.filter(pk=song_id).exists():
        already_fav = True
    else:
        user.fav_songs.add(song)
        user.save()
    data = {
        'added': True,
        'already_fav': already_fav
    }
    return JsonResponse(data)


def remove_song(request):
    if not request.is_ajax():
        return render(request, 'error.html', {
            'error_title': 'Only Ajax is allowed here',
            'error_body': 'For some reason you managed to access this route <br /> but we\'re sorry to inform you '
                          'that this route accepts only ajax requests '
        })
    user_id = request.GET.get('user_id')
    song_id = request.GET.get('song_id')

    user = ElmusicUser.objects.filter(pk=user_id)
    if len(user) == 0:
        data = {
            'added': False,
            'message': 'Invalid User',
        }
        return JsonResponse(data)
    user = user[0]
    song = Song.objects.filter(pk=song_id)
    if len(song) == 0:
        data = {
            'added': False,
            'message': 'Invalid Song',
        }
        return JsonResponse(data)
    song = song[0]
    already_removed = False
    if not user.fav_songs.filter(pk=song_id).exists():
        already_removed = True
    else:
        user.fav_songs.remove(song)
        user.save()
    data = {
        'removed': True,
        'already_fav': already_removed
    }
    return JsonResponse(data)


def add_artist(request):
    if not request.is_ajax():
        return render(request, 'error.html', {
            'error_title': 'Only Ajax is allowed here',
            'error_body': 'For some reason you managed to access this route <br /> but we\'re sorry to inform you '
                          'that this route accepts only ajax requests '
        })
    user_id = request.GET.get('user_id')
    artist_id = request.GET.get('artist_id')

    user = ElmusicUser.objects.filter(pk=user_id)
    if len(user) == 0:
        data = {
            'added': False,
            'message': 'Invalid User',
        }
        return JsonResponse(data)
    user = user[0]
    artist = Artist.objects.filter(pk=artist_id)
    if len(artist) == 0:
        data = {
            'added': False,
            'message': 'Invalid Artist',
        }
        return JsonResponse(data)
    artist = artist[0]
    already_fav = False
    if user.fav_artists.filter(pk=artist_id).exists():
        already_fav = True
    else:
        user.fav_artists.add(artist)
        user.save()
    data = {
        'added': True,
        'already_fav': already_fav
    }
    return JsonResponse(data)


def remove_artist(request):
    if not request.is_ajax():
        return render(request, 'error.html', {
            'error_title': 'Only Ajax is allowed here',
            'error_body': 'For some reason you managed to access this route <br /> but we\'re sorry to inform you '
                          'that this route accepts only ajax requests '
        })
    user_id = request.GET.get('user_id')
    artist_id = request.GET.get('artist_id')

    user = ElmusicUser.objects.filter(pk=user_id)
    if len(user) == 0:
        data = {
            'added': False,
            'message': 'Invalid User',
        }
        return JsonResponse(data)
    user = user[0]
    artist = Artist.objects.filter(pk=artist_id)
    if len(artist):
        data = {
            'added': False,
            'message': 'Invalid Artist',
        }
        return JsonResponse(data)
    artist = artist[0]
    already_removed = False
    if not user.fav_artists.filter(pk=artist_id).exists():
        already_removed = True
    else:
        user.fav_artists.remove(artist)
        user.save()
    data = {
        'removed': True,
        'already_fav': already_removed
    }
    return JsonResponse(data)


def add_album(request):
    if not request.is_ajax():
        return render(request, 'error.html', {
            'error_title': 'Only Ajax is allowed here',
            'error_body': 'For some reason you managed to access this route <br /> but we\'re sorry to inform you '
                          'that this route accepts only ajax requests '
        })
    user_id = request.GET.get('user_id')
    album_id = request.GET.get('album_id')

    user = ElmusicUser.objects.filter(pk=user_id)
    if len(user):
        data = {
            'added': False,
            'message': 'Invalid User',
        }
        return JsonResponse(data)
    user = user[0]
    album = Album.objects.filter(pk=album_id)
    if len(album) == 0:
        data = {
            'added': False,
            'message': 'Invalid Album',
        }
        return JsonResponse(data)
    album = album[0]
    already_fav = False
    if user.fav_albums.filter(pk=album_id).exists():
        already_fav = True
    else:
        user.fav_albums.add(album)
        user.save()
    data = {
        'added': True,
        'already_fav': already_fav
    }
    return JsonResponse(data)


def remove_album(request):
    if not request.is_ajax():
        return render(request, 'error.html', {
            'error_title': 'Only Ajax is allowed here',
            'error_body': 'For some reason you managed to access this route <br /> but we\'re sorry to inform you '
                          'that this route accepts only ajax requests '
        })
    user_id = request.GET.get('user_id')
    album_id = request.GET.get('album_id')

    user = ElmusicUser.objects.filter(pk=user_id)
    if len(user) == 0:
        data = {
            'added': False,
            'message': 'Invalid User',
        }
        return JsonResponse(data)
    user = user[0]
    album = Album.objects.filter(pk=album_id)
    if len(album) == 0:
        data = {
            'added': False,
            'message': 'Invalid Album',
        }
        return JsonResponse(data)
    album = album[0]
    already_removed = False
    if not user.fav_albums.filter(pk=album_id).exists():
        already_removed = True
    else:
        user.fav_albums.remove(album)
        user.save()
    data = {
        'removed': True,
        'already_fav': already_removed
    }
    return JsonResponse(data)


def remove_review(request, id):
    user = request.user
    review = Review.objects.filter(pk=id)
    if len(review) == 0:
        return render(request,'error.html',{
            'error_title': 'Request Error',
            'error_body': 'You request contained an error: Review not found'
        })
    review = review[0]
    username = user.username.strip(' ')
    person = review.person.strip(' ')
    if review.album is not None:
        album_id = review.album.id
        if username == person:
            album = Album.objects.filter(pk=album_id)[0]
            album.review_set.remove(review)
            album.save()
        return redirect('main:show_album', id=album_id)
    elif review.artist is not None:
        artist_id = review.artist.id
        if username == person:
            artist = Artist.objects.filter(pk=artist_id)[0]
            artist.review_set.remove(review)
            artist.save()
        return redirect('main:show_artist', id=artist_id)
    else:
        song_id = review.song.id
        if username == person:
            song = Song.objects.filter(pk=song_id)[0]
            song.review_set.remove(review)
            song.save()
        return redirect('main:show_song', id=song_id)
