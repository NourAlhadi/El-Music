from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Artist " + self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return "Album " + str(self.title) + " By " + str(self.artist)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title) + " By " + str(self.album.artist)
