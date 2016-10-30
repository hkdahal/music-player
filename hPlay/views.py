from django.shortcuts import render

from hPlay.models import Song, Artist, Playlist, Video


def index(request):
    bipul_songs = Song.objects.filter(artist__first_name__iexact="bipul")
    videos = Video.objects.all()
    return render(request, 'hPlay/base.html', context={
        'playlist': bipul_songs,
        'videos': videos})


def songs_per_artist(request, name):
    songs = Song.objects.filter(
        artist__first_name__icontains=name.split()[0]).order_by('title')
    cover = Artist.objects.filter(
        first_name__icontains=name.split()[0])[0].image
    cover = 'posters/artists/'+cover
    return render(request,
                  'hPlay/content_page.html',
                  context={'playlist': songs, 'cover': cover})


def songs_per_playlist(request, name):
    songs = Song.objects.filter(playlist__name=name)
    cover = Playlist.objects.filter(name=name)[0].cover_art
    cover = 'posters/cover arts/' + cover
    return render(request,
                  'hPlay/content_page.html',
                  context={'playlist': songs, 'cover': cover})


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
    cover = 'posters/cover arts/All.jpg'
    return render(request, 'hPlay/content_page.html',
                  context={'playlist': songs, 'cover': cover})


def error_404(request):
    return render(request, 'hPlay/content_page.html', context={'errors': True})
