from app.kinopoisk import KinoPoisk
from pathlib import Path
import json


class Movie:

    __temp = ''

    @staticmethod
    def get(name):
        data = {}
        file = Path(Movie.__temp + name + '.list')
        if file.is_file():
            with file.open() as f:
                data['list'] = json.load(f)
        else:
            file = Path(Movie.__temp + name + '.film')
            if file.is_file():
                with file.open() as f:
                    data['mov'] = json.load(f)
            else:
                data['list'] = KinoPoisk.search(name)
        return data

    @staticmethod
    def set(name,new_id):
        return

    @staticmethod
    def delete(name):
        return