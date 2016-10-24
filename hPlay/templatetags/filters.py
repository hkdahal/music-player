from django import template

from hPlay.models import Song, Artist, Playlist

register = template.Library()


@register.filter
def featured_artists(something):
    return Artist.objects.all()


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


@register.filter
def mod_true(num, mod_by):
    if num % mod_by == 1:
        return True
    else:
        return False
