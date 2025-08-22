from rest_framework import serializers
from .models import Artist, Album, Song, AlbumSong

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title']

class AlbumSongSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)
    
    class Meta:
        model = AlbumSong
        fields = ['track_number', 'song']

class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name', read_only=True)
    tracks = AlbumSongSerializer(many=True, read_only=True, source='tracks')
    
    class Meta:
        model = Album
        fields = ['id', 'title', 'artist_name', 'release_year', 'tracks']

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    
    class Meta:
        model = Artist
        fields = ['id', 'name', 'albums']