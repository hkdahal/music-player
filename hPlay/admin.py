from django.contrib import admin

from hPlay.models import Song, Playlist, Artist, Video

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Artist)
admin.site.register(Video)
