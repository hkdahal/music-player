from django import template

from hPlay.models import Song, Artist, Playlist

register = template.Library()


@register.filter
def featured_artists(something):
    return Artist.objects.all()[:int(something)]


@register.filter
def discover_playlist(something):
    playlists = Playlist.objects.all()
    return playlists[:3]


@register.filter
def new_releases(something):
    playlists = Playlist.objects.all()
    artists = Artist.objects.all()

    artists.extend(playlists)

    return artists[:8]