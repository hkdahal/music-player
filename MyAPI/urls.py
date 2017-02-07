from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^playlists',
        views.ListPlaylist.as_view(),
        name='playlists'
        ),

    url(r'^songs',
        views.ListSongs.as_view(),
        name='songs'
        ),
    url(r'^artists',
        views.ListArtists.as_view(),
        name='artists'
        ),
    url(r'^videos',
        views.ListVideos.as_view(),
        name='videos'
        ),
]
