import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Bugs2(object):

    url = ''
    hdr = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'

    def set_class_name(self, class_name):
        self.class_name = class_name

    def get_ranking(self):
        req = urllib.request.Request(self.url, headers=self.hdr)
        html = urllib.request. urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        print('--------TITLE---------')
        ls = soup.find_all("div", {"class": self.class_name[0]})
        for i in ls:
            print(f' {i.find("a").text}')
        print('--------ARTIST---------')
        for i in ls:
            print(f' {i.find("a").text}')

    @staticmethod
    def main():
        b = Bugs2()
        lst50 = soup.select('.lst50,.lst100')
        melonList = []
        while 1:
            menu = input('0, 1-input, 2-output')
            if menu == '1':
                b.set_url(input('time 예) 2021052511'))

            elif menu == '2':
                for i in lst50:
                    temp = []
                    temp.append(i.select_one('.rank').text)
                    temp.append(i.select_one('.ellipsis.rank01').a.text)
                    temp.append(i.select_one('.ellipsis.rank02').a.text)
                    temp.append(i.select_one('.ellipsis.rank03').a.text)
                    melonList.append(temp)
            else:
                print('error')


Bugs2.main()