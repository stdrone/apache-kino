import os, tempfile, json


class MovieList:
    __name: str
    __list: list = ()

    def __path(self):
        temp = tempfile.gettempdir() + '/cinema/'
        if not os.path.exists(temp):
            os.makedirs(temp)
        return temp + self.__name + '.list'

    def __read(self):
        file = self.__path()
        if os.path.isfile(file):
            f = open(file, 'r')
            self.__list = json.load(f)
            f.close()

    def __init__(self, name):
        self.__name = name
        self.__read()
