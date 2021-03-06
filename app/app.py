from app.movie import Movie
from app.list import List
import json


class App:
    __method = ''
    __data = {}

    def __init__(self, method, content):
        self.__method = method
        data = content.decode("utf-8")
        if data != '':
            self.__data = json.loads(data)

    def process(self):
        result = {}
        if self.__method == 'OPTIONS':
            return result
        if 'list' in self.__data:
            list = List(self.__data['list'])
            result = list.list()
        else:
            movie = Movie(self.__data['name'])
            if self.__method == 'POST':
                result = movie.get()
            elif self.__method == 'PUT':
                result = movie.set(self.__data['id'])
            elif self.__method == 'DELETE':
                if self.__data['file']:
                    result = movie.delete()
                else:
                    result = movie.clear()
        return json.dumps(result)
