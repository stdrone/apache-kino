from app.movie import Movie


class App:
    @staticmethod
    def process(request, data):
        if request == 'POST':
            return Movie.get(data['name'])
        elif request == 'PUT':
            return Movie.set(data['name'],data['id'])
        elif request == 'DELETE':
            if data['file']:
                return Movie.delete(data['name'])
            else:
                return Movie.clear(data['name'])
        return {}
