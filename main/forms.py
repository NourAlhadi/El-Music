from django import forms
from .models import Artist, Album, Song


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'image', )


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'genre', 'logo', )
        widgets = {
            'artist': forms.Select(attrs={'class': 'col-lg-8'}),
            'title': forms.TextInput(attrs={'class': 'col-lg-8'}),
            'genre': forms.TextInput(attrs={'class': 'col-lg-8'}),
            'logo': forms.FileField(attrs={'class': 'col-lg-3'})
        }


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('album', 'title', 'file_src', )
