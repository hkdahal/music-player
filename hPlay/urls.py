from django.conf.urls import url
from hPlay import views

app_name = 'hPlay'
urlpatterns = [
    url(r'^$', views.index, name='Homepage'),

    url(r'^playlist/(?P<name>\D+)/',
        views.songs_per_playlist,
        name='playlist songs'),

    url(r'^artist/(?P<name>\D+)/',
        views.songs_per_artist,
        name='artist songs'),

    url(r'^artists', views.artists, name='Artists'),

    url(r'^playlists', views.playlists, name='Playlist'),

    url(r'^songs', views.songs, name='Songs'),

    url(r'^404/', views.error_404, name="404")
]
