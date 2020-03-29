import os.path, os

class List:
    __name = ''
    __data = dict()

    def __init__(self, name):
        self.__name = name
        
    def __path(self):
        path = os.environ.get('CINEMAPATH')
        return path + '/' + self.__name

    def list(self):
        path = self.__path()
        self.__data.list = [f for f in listdir(path) if f not in ('test', 'app', 'search.wsgi') and f[0] != '.']
        return self.__data