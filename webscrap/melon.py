import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
class Bugs2(object):
    url = ''
    hdr = { 'User-Agent' : 'Mozilla/5.0' }
    class_name = []
    def set_url(self, time):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'
    def set_class_name(self, class_name):
        self.class_name = class_name
    def get_ranking(self):
        result = []
        bs = BeautifulSoup(urlopen(self.url), 'html.parser')
        ls = bs.find_all(name='div', attrs=({'class':'ellipsis rank01'}))
        for i in ls:
            i.find('a').text()
            result.append(i)
        return result
    @staticmethod
    def main():
        b = Bugs2()
        while 1:
            menu = input('0, 1-input time, 2-output')
            if menu == '1':
                b.set_url(input('time  예) 2021052511'))
            elif menu == '2':
                b.get_ranking()