import json


class HttpData:

    __method: str
    __name: str
    __id: str
    __withFile: bool

    @property
    def method(self):
        return self.__method

    @property
    def name(self):
        return self.__name

    @property
    def withFile(self):
        return self.__withFile

    @property
    def id(self):
        return self.__id

    def __init__(self, environ):
        self.__method = environ['REQUEST_METHOD']
        try:
            body_size = int(environ.get('CONTENT_LENGTH', 0))
            data = environ['wsgi.input'].read(body_size)
            data = data.decode("utf-8")
            if data != '':
                data = json.loads(data)
                self.__name = data.get('name')
                self.__id = data.get('id')
                self.__withFile = data.get('file')
        except ValueError:
            return
