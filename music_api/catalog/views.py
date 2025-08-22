from rest_framework import viewsets
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().prefetch_related('albums__tracks__song')
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().prefetch_related('tracks__song')
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().prefetch_related('album_entries__album__artist')
    serializer_class = SongSerializer