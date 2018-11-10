from app.kinopoisk import KinoPoisk
import os.path, json, os
from deluge_client import DelugeRPCClient


class Movie:

    __name = ''
    __data = dict()

    def __init__(self, name):
        self.__name = name
        self.__read()

    def __path(self):
        path = os.environ.get('STORAGE') + '/kino/'
        if not os.path.exists(path):
            os.mkdir(path)
        return path + self.__name + '.list'

    def __read(self):
        file = self.__path()
        if os.path.isfile(file):
            f = open(file, 'r')
            self.__data = json.load(f)
            f.close()
        else:
            self.__data = dict()

    def __save(self):
        file = self.__path()
        f = open(file, 'w+')
        f.write(json.dumps(self.__data))
        f.close()

    def deluge(self):
        deluge_rpc = os.environ.get('DELUGE_ADDRESS')
        if deluge_rpc is not None:
            client = DelugeRPCClient(
                deluge_rpc,
                int(os.environ.get('DELUGE_PORT')),
                os.environ.get('DELUGE_USER'),
                os.environ.get('DELUGE_PASS')
            )
            client.connect()
            return client
        return None

    def __get_hash(self):
        if self.__data.get('hash') is None:
            #self.__data['files'] = {}
            #self.__data['name'] = self.__name
            client = self.deluge()
            if client is not None:
                torrents = client.call('core.get_torrents_status', {}, ['name', 'files'])
                for key, torrent in torrents.items():
                    for file in torrent[b'files']:
                        file_name = file[b'path'].decode("utf-8")
                        #self.__data['files'][key.decode("utf-8")] = file_name
                        if self.__name in file_name:
                            self.__data['hash'] = key.decode("utf-8")
                            self.__save()
                            break

    def __get_progress(self):
        file_hash = self.__data.get('hash')
        if file_hash is not None and self.__data.get('movie') is not None:
            progress = self.__data['movie'].get('progress')
            if progress is None or progress < 100:
                client = self.deluge()
                if client is not None:
                    data = client.call('core.get_torrents_status', {'id': file_hash}, ['progress'])
                    for key, torrent in data.items():
                        self.__data['movie']['progress'] = torrent[b'progress']
                        self.__save()

    def get(self):
        if len(self.__data) == 0:
            self.__data['list'] = KinoPoisk.search(self.__name)
            self.__save()
        if 'movie' in self.__data and self.__data['movie'] is not None:
            self.__get_hash()
            self.__get_progress()
        return self.__data

    def set(self,new_id):
        if new_id == '0':
            self.__data = {'movie': None}
        else:
            self.__data = {'movie': KinoPoisk.get(new_id)}
            self.__get_hash()
            self.__save()
        return self.__data

    def delete(self):
        result = dict()
        if self.__data.get('hash') is not None:
            client = self.deluge()
            if client is not None:
                result['delete'] = client.call('core.remove_torrent', self.__data.get('hash'), True)
                self.clear()
        return result

    def clear(self):
        os.remove(self.__path())
        return {}
