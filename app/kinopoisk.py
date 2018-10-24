import pycurl
import io
import urllib


class KinoPoisk:

    __cookie = ''

    def __curl(self, url):
        response = io.StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, response.write)
        c.setopt(c.HTTPHEADER, ['Content-Type: application/json', 'Accept-Charset: UTF-8'])
        c.setopt(c.HTTPGET, 1)
        c.setopt(c.COOKIEFILE, KinoPoisk.__cookie)
        c.setopt(c.HTTPHEADER,  [
                'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
                'Host: www.kinopoisk.ru',
                "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
                'Upgrade-Insecure-Requests:1',
                'Referer: https://www.kinopoisk.ru/'
            ])
        c.setopt(c.SSL_VERIFYPEER, 0)
        c.setopt(c.FOLLOWLOCATION, 1)
        c.setopt(c.HEADER, 1)
        c.perform()
        c.close()
        return response.getvalue()

    def __init__(self):
        return

    def search(self,name):
        html = self.__curl('http://www.kinopoisk.ru/index.php?first=no&what=&kp_query=' + urllib.parse.urlencode(name))
        return {}

    def get(self,get_id):
        html = self.__curl('https://www.kinopoisk.ru/film/' + get_id  + '/')
        return {}
