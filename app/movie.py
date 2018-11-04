import os.path, tempfile, kinopoisk, json
from kinopoisk import movie
from app.nameconverter import NameConverter


class Movie:

    id: str
    description: str
    genre: str
    name: str
    name: str
    rate: float
    rating: str

    def __init__(self, name: str):
        self = Movie.__get(name)

    def __save(self):
        file = Movie.__path(self.name)
        f = open(file, 'w+')
        f.write(json.dumps(self))
        f.close()

    @staticmethod
    def get(name):
        data = {}
        file = Movie.__path(name)
        else:
            converter = NameConverter(name)
            list = []
            for kino in converter:
                list += movie.Movie.objects.search(kino)
            data['list'] = list
            Movie.__write(file, data)
        return data

    @staticmethod
    def set(name,new_id):
        if new_id == '0':
            data = {'movie': None}
        else:
            data = {'movie': None}
        file = Movie._path(name)
        Movie._write(file, data)
        return data

    @staticmethod
    def delete(name):
        Movie.clear(name)
        return {}

    @staticmethod
    def clear(name):
        os.remove(Movie._path(name))
        return {}
