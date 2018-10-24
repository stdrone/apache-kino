from app.kinopoisk import KinoPoisk
from pathlib import Path
import json


class Movie:

    __temp = ''

    def __init__(self):
        return

    def get(self,name):
        data = {}
        file = Path(self.__temp + name + '.list')
        if file.is_file():
            with file.open() as f:
                data['list'] = json.load(f)
        else:
            file = Path(self.__temp + name + '.film')
            if file.is_file():
                with file.open() as f:
                    data['mov'] = json.load(f)
            else:
                kino = KinoPoisk()
                data['list'] = kino.search(name)
        return data

    def set(self,name,new_id):
        return

    def delete(self,name):
        return