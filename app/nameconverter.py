import cyrtranslit
import re


class NameConverter:
    __name = None

    def __init__(self, name):
        self.__name = name

    def __iter__(self):
        replace = [
            func for func in dir(ReplaceFunctions)
            if callable(getattr(ReplaceFunctions, func))
            and func.replace('_ReplaceFunctions','').startswith('__replace')
        ]
        self.__step = iter(replace)
        self.__newName = self.__name
        return self

    def __next__(self):
        replace_func = next(self.__step)
        method = getattr(ReplaceFunctions, replace_func)
        self.__newName = method(self.__newName)
        return self.__newName


class ReplaceFunctions:
    @staticmethod
    def __replace1(name):
        name = re.sub('20\d\d.*', '', name)
        name = re.sub('19\d\d', '', name)
        name = re.sub('\[NNM.*?\]', '', name)
        name = re.sub('(Season|Сезон|DVD|HDR|DUB|HDT|\.m4v|\.avi)', '', name)
        name = name.replace('.', ' ').replace('_', ' ')
        return name

    @staticmethod
    def __replace2(name):
        return name

    @staticmethod
    def __replace3(name):
        return name.replace('-',' ').replace('1','i').replace('0','o').replace('.',' ')

    @staticmethod
    def __replace4(name):
        name = name.replace('’','ь').replace('ya','я')
        name = cyrtranslit.to_cyrillic(name,'ru')
        return name

    @staticmethod
    def __replace5(name):
        return name.replace('ы','й')
