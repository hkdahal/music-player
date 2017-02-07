from rest_framework import serializers

from hPlay import models


class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Playlist


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Artist


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Song


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Video
