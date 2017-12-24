from django import forms
from .models import Artist, Album, Song


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'image', )
    name = forms.CharField(label='Artist Name', widget=forms.TextInput(attrs={'placeholder': 'Artist name'}))
    image = forms.FileField(label='Artist Image')


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'genre', 'logo', )
    title = forms.CharField(label='Album Title', widget=forms.TextInput(attrs={'placeholder': 'Album title'}))
    genre = forms.CharField(label='Album Genre', widget=forms.TextInput(attrs={'placeholder': 'Album genre'}))
    logo = forms.FileField(label='Album Logo')


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('album', 'title', 'file_src', )
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Song title'}))
    file_src = forms.FileField(label='File Source')