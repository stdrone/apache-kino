from app.movie import Movie
from app.httpdata import HttpData


class App:
    @staticmethod
    def process(request: HttpData):
        if request.method == 'POST':
            return Movie.get(request.name)
        elif request == 'PUT':
            return Movie.set(request.name, request.id)
        elif request == 'DELETE':
            if request.withFile:
                return Movie.delete(request.name)
            else:
                return Movie.clear(request.name)
        return {}
