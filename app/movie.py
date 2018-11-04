from app.kinopoisk import KinoPoisk
import os.path, json, tempfile


class Movie:

    @staticmethod
    def _path(name):
        path = tempfile.gettempdir() + '/kino/'
        if not os.path.exists(path):
            os.mkdir(path)
        return path + name + '.list'

    @staticmethod
    def _read(file):
        f = open(file, 'r')
        data = json.load(f)
        f.close()
        return data

    @staticmethod
    def _write(file, data):
        f = open(file, 'w+')
        f.write(json.dumps(data))
        f.close()

    @staticmethod
    def get(name):
        data = {}
        file = Movie._path(name)
        if os.path.isfile(file):
            data = Movie._read(file)
        else:
            data['list'] = KinoPoisk.search(name)
            Movie._write(file, data)
        return data

    @staticmethod
    def set(name,new_id):
        if new_id == '0':
            data = {'movie': None}
        else:
            data = {'movie': KinoPoisk.get(new_id)}
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
