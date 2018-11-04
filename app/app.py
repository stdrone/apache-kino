from app.movie import Movie
import json


class App:
    __method = ''
    __data = dict()

    def __init__(self, method, content):
        self.__method = method
        data = content.decode("utf-8")
        if data != '':
            self.__data = json.loads(data)

    def process(self):
        result = {}
        if self.__method == 'POST':
            result = Movie.get(self.__data['name'])
        elif self.__method == 'PUT':
            result = Movie.set(self.__data['name'],self.__data['id'])
        elif self.__method == 'DELETE':
            if self.__data['file']:
                result = Movie.delete(self.__data['name'])
            else:
                result = Movie.clear(self.__data['name'])
        return json.dumps(result)
