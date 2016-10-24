from django.shortcuts import render

from hPlay.models import Song, Artist, Playlist, Video


def index(request):
    bipul_songs = Song.objects.filter(artist__first_name__iexact="bipul")
    videos = Video.objects.all()[:3]
    return render(request, 'hPlay/base.html', context={
        'playlist': bipul_songs,
        'videos': videos})


def songs_per_artist(request, name):
    songs = Song.objects.filter(artist__first_name__icontains=name.split()[0])
    return render(request,
                  'hPlay/content_page.html',
                  context={'playlist': songs})


def songs_per_playlist(request, name):
    songs = Song.objects.filter(playlist__name=name)
    return render(request,
                  'hPlay/content_page.html',
                  context={'playlist': songs})


def artists(request):

    english_artists = Artist.objects.filter(language='English')
    nepali_artists = Artist.objects.filter(language='Nepali')
    hindi_artists = Artist.objects.filter(language='Hindi')

    return render(request,
                  'hPlay/content_page.html',
                  context={'artists': True,
                           'english_artists': english_artists,
                           'nepali_artists': nepali_artists,
                           'hindi_artists': hindi_artists,
                           })


def playlists(request):

    playlist_list = Playlist.objects.all()

    return render(request,
                  'hPlay/content_page.html',
                  context={'playlists': True, 'playlist_list': playlist_list})


def songs(request):
    songs = Song.objects.all().order_by('title')

    return render(request, 'hPlay/content_page.html', context={'playlist': songs})


def error_404(request):
    return render(request, 'hPlay/content_page.html', context={'errors': True})