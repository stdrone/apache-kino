from app.movie import Movie
from app.kinopoisk import KinoPoisk

#__temp = 'C:/temp/kino/'
__temp = '/home/user/tmp/kino'
Movie.temp = __temp
KinoPoisk.temp = __temp + 'cookie.txt'
