import json


class HttpData:

    __environ = []
    __bodySize = 0

    def __init__(self, environ):
        self.__environ = environ
        try:
            self.__bodySize = int(self.__environ.get('CONTENT_LENGTH', 0))
        except ValueError:
            self.__bodySize = 0

    def body(self):
        data = self.__environ['wsgi.input'].read(self.__bodySize)
        data = data.decode("utf-8")
        if data == '':
            return dict()
        return json.loads(data)

    def request(self):
        return self.__environ['REQUEST_METHOD']

    @staticmethod
    def response(data):
        return json.dumps(data)