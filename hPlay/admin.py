from django.contrib import admin

from hPlay.models import Song, Playlist, Artist

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Artist)