from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    release_year = models.IntegerField()
    
    class Meta:
        unique_together = ('artist', 'title')
    
    def __str__(self):
        return f"{self.title} - {self.artist.name}"

class Song(models.Model):
    title = models.CharField(max_length=255)
    albums = models.ManyToManyField(Album, through='AlbumSong')
    
    def __str__(self):
        return self.title

class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='album_entries')
    track_number = models.PositiveIntegerField()
    
    class Meta:
        unique_together = (('album', 'track_number'), ('album', 'song'))
    
    def __str__(self):
        return f"{self.album.title} - {self.track_number}. {self.song.title}"
