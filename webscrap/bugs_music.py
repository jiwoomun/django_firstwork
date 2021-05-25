from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic(object):

    url = ''


    def __str__(self):
        return self.url

    @staticmethod
    def scrap(url, class_name):
        soup = BeautifulSoup(urlopen(url), 'lxml')
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": class_name[0]})): #artist
            count += 1
            print(f'{str(count)} RANKING')
            print(f'{class_name}: {i.find("a").text}')

# https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = int(input('0.Exit\n 1.Input URL\n 2.Get Ranking \n 3.'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('input URL')

            elif menu == 2:
                print(f'Input URL is {bugs}')

            else:
                print('Wrong Number')
                continue

BugsMusic.main()