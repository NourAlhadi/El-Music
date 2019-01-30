from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='artists/')
    bio = models.TextField(max_length=15000, default="")

    def __str__(self):
        return "Artist " + self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    desc = models.TextField(max_length=15000, default="")
    logo = models.FileField(upload_to='albums/')

    def __str__(self):
        return "Album " + str(self.title) + " By " + str(self.artist)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_src = models.FileField(upload_to='songs/')
    title = models.CharField(max_length=50)
    lyrics = models.TextField(max_length=15000, default="")

    def __str__(self):
        return str(self.title) + " By " + str(self.album.artist)


class Review(models.Model):
    stars = models.IntegerField(default=3, blank=False)
    body = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    person = models.CharField(max_length=50, default="")
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.stars) + " review made by " + str(self.person)
