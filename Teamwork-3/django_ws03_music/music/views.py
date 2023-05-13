from rest_framework.decorators import api_view
from .models import (
    Artist,
    Album,
    Song,

)
from .serializers import (
    ArtistSerializer,
    AlbumSerializer,
    SongSerializer,
    SongWithLyricsSerializer,
    AlbumWithSongsSerializer
)

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

class ArtistListCreateView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumListCreateView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongListCreateView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongWithLyricsListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongWithLyricsSerializer
    
class AlbumWithSongListView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumWithSongsSerializer