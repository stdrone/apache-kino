from app.movie import Movie
from app.kinopoisk import KinoPoisk
import os
import tempfile


__temp = tempfile.gettempdir() + '/kino/'
if not os.path.exists(__temp):
    os.makedirs(__temp)
Movie.temp = __temp
KinoPoisk.temp = __temp + 'cookie.txt'
