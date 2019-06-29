import pycurl
import io
import re
import cyrtranslit
from urllib import parse


class KinoPoisk:

    cookie = ''

    @staticmethod
    def __curl(url):
        response = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, response.write)
        c.setopt(c.HTTPGET, 1)
        c.setopt(c.COOKIEFILE, KinoPoisk.cookie)
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
        try:
            data = data.decode('cp1251')
        except:
            data = data.decode('utf8')
        return data

    @staticmethod
    def __get_list(name):
        search = 'https://www.kinopoisk.ru/index.php?first=no&what=&kp_query=' + parse.quote_plus(name)
        html = KinoPoisk.__curl(search)
        films = re.findall('data-id=\"(.*?)\".*data-type\=\"(series|film)\".*\>([^\<]+?)\<\/a.*\"year\">(.*?)<\/', html)
        return films

    @staticmethod
    def __parse(regexp, html):
        if not isinstance(html, str):
            return None
        data = re.findall(regexp, html)
        if type(data) is tuple:
            if type(data[0]) is tuple:
                return data[0][0]
            else:
                return data[0]
        else:
            return data

    @staticmethod
    def search(name):
        films = KinoPoisk.__get_list(name)
        name = name.replace('-',' ').replace('1','i').replace('0','o').replace('.',' ');
        films += KinoPoisk.__get_list(name)
        name = name.replace('’','ь').replace('ya','я')
        name = cyrtranslit.to_cyrillic(name,'ru')
        films += KinoPoisk.__get_list(name)
        name = name.replace('ы','й')
        films += KinoPoisk.__get_list(name)
        films = list(set(films))
        return films

    @staticmethod
    def get(get_id):
        data = {}
        search = 'https://www.kinopoisk.ru/film/' + get_id + '/'
        html = KinoPoisk.__curl(search)

        data['id'] = get_id
        data['description'] = KinoPoisk.__parse('\<div.*?\"description\"\.*?\>(.*?)\<\/div', html)

        genre = KinoPoisk.__parse('itemprop=\"genre\".*?<\/span', html)
        data['genre'] = KinoPoisk.__parse('<a.*?>(.*?)<\/a', genre[0])

        data['name'] = KinoPoisk.__parse('\<span.*?\"moviename-title-wrapper\"\>(.*?)\<\/span', html)
        data['rate'] = KinoPoisk.__parse('\<span.*?\"rating_ball\"\>(.*?)\<\/span', html)

        data['rating'] = ''
        rating = KinoPoisk.__parse('(\<img src=\".*?\/mpaa\/.*?\".*?\>)', html)
        if len(rating) > 0:
            data['rating'] += rating[0]
        rating = KinoPoisk.__parse('(\<div class=\"ageLimit.*?\".*?\/div\>)', html)
        if len(rating) > 0:
            data['rating'] += rating[0]

        return data
