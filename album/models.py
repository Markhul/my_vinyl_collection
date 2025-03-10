from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    genre = models.CharField(max_length=150)

    def __str__(self):
        return self.genre
    

class Album(models.Model):
    band_name = models.ForeignKey(Band, on_delete=models.PROTECT, related_name="album")
    album = models.CharField(max_length=300)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="album")
    year = models.IntegerField()
    tracks = models.TextField(blank=True, null=True)
    lineup = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='img/covers/', blank=True, null=True)

    def __str__(self):
        return self.album
