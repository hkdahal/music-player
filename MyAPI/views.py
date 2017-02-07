from rest_framework import generics
# from django.shortcuts import get_object_or_404


from hPlay import models
from . import serializers


class ListPlaylist(generics.ListAPIView):
    queryset = models.Playlist.objects.all()
    serializer_class = serializers.PlaylistSerializer


class ListSongs(generics.ListAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer


class ListArtists(generics.ListAPIView):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer


class ListVideos(generics.ListAPIView):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer


