from app.kinopoisk import KinoPoisk
import os.path, json, tempfile, os
from deluge_client import DelugeRPCClient


class Movie:

    __name = ''
    __data = dict()

    def __init__(self, name):
        self.__name = name
        self.__read()

    def __path(self):
        path = tempfile.gettempdir() + '/kino/'
        if not os.path.exists(path):
            os.mkdir(path)
        return path + self.__name + '.list'

    def __read(self):
        file = self.__path()
        if os.path.isfile(file):
            f = open(file, 'r')
            self.__data = json.load(f)
            f.close()

    def __save(self):
        file = self.__path()
        f = open(file, 'w+')
        f.write(json.dumps(self.__data))
        f.close()

    def deluge(self):
        client = DelugeRPCClient(
            '127.0.0.1',
            58846,
            'torrent',
            'torrent'
        )
        client.connect()
        return client

    def __get_hash(self):
        if self.__data.get('hash') is None:
            #self.__data['files'] = {}
            #self.__data['name'] = self.__name
            torrents = self.deluge().call('core.get_torrents_status', {}, ['name', 'files'])
            for key, torrent in torrents.items():
                for file in torrent[b'files']:
                    file_name = file[b'path'].decode("utf-8")
                    #self.__data['files'][key.decode("utf-8")] = file_name
                    if self.__name in file_name:
                        self.__data['hash'] = key.decode("utf-8")
                        self.__save()
                        break

    def get(self):
        if len(self.__data) == 0:
            self.__data['list'] = KinoPoisk.search(self.__name)
            self.__save()
        self.__get_hash()
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
            result['delete'] = self.deluge().call('core.remove_torrent', self.__data.get('hash'), True)
            self.clear()
        return result

    def clear(self):
        os.remove(self.__path())
        return {}
