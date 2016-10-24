from django.db import models

LANGUAGE_CHOICES = (
    ("English", "English"),
    ("Nepali", "Nepali"),
    ("Hindi", "Hindi"),
    ("Dzongkha", "Dzongkha")
)

GENRE_CHOICES = (
    ("Unknown", "Unknown"),
    ("Movie", "Movie"),
    ("Pop", "Pop"),
    ("Rock", "Rock"),
    ("Alternative/Indie", "Alternative/Indie"),
    ("Remix", "Remix"),
    ("Instrumental", "Instrumental"),
    ("Folk", "Folk"),
    ("Electronic", "Electronic")
)


class Playlist(models.Model):
    name = models.CharField(max_length=1000)
    cover_art = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000, blank=True)
    image = models.CharField(max_length=2000, blank=True)
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])

    def __str__(self):
        return self.first_name + " " + self.last_name


class Song(models.Model):
    title = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist, blank=True)
    url = models.CharField(max_length=1000)
    playlist = models.ManyToManyField(Playlist)
    genre = models.CharField(max_length=50,
                             choices=GENRE_CHOICES,
                             default=GENRE_CHOICES[0][0])
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist)
    url = models.CharField(max_length=1000)
    genre = models.CharField(max_length=50,
                             choices=GENRE_CHOICES,
                             default=GENRE_CHOICES[0][0])
    language = models.CharField(max_length=10,
                                choices=LANGUAGE_CHOICES,
                                default=LANGUAGE_CHOICES[0][0])
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.title


