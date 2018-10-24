import pycurl
import io
from urllib import parse


class KinoPoisk:

    __cookie = ''

    @staticmethod
    def __curl(url):
        response = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, response.write)
        c.setopt(c.HTTPGET, 1)
        c.setopt(c.COOKIEFILE, KinoPoisk.__cookie)
        c.setopt(c.ENCODING, 'gzip, deflate')
        c.setopt(c.HEADER, 0)
        c.setopt(c.HTTPHEADER,  [
                'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
                'Host: www.kinopoisk.ru',
                "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
                'Upgrade-Insecure-Requests:1',
                'Referer: https://www.kinopoisk.ru/',
                'Accept-Charset: windows-1251'
            ])
        c.setopt(c.MAXREDIRS, 50)
        c.setopt(c.FOLLOWLOCATION, 1)
        c.setopt(c.SSL_VERIFYPEER, 0)
        c.perform()
        c.close()
        data = response.getvalue()
        data = data.decode('cp1251')
        return data

    @staticmethod
    def search(name):
        html = KinoPoisk.__curl('https://www.kinopoisk.ru/index.php?first=no&what=&kp_query=' + parse.quote_plus(name))
        return {}

    @staticmethod
    def get(get_id):
        html = KinoPoisk.__curl('https://www.kinopoisk.ru/film/' + get_id  + '/')
        return {}
