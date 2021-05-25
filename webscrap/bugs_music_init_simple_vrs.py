from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic(object):

    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def scrap(soup):
        print('-------------- ARTIST RANKING ----------------')
        count = 0
        for i in soup.find_all(for i in (name='p', attrs=({"class":()})):
            count += 1
            print(f'{str(count)} RANKING')
            print(f'ARTIST: {i.find("a").text}')

"""
        print('-------------- TITLE RANKING ----------------')
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": "title"})):
            count += 1
            print(f'{str(count)} RANKING')
            print(f'TITLE: {i.find("a").text}')
"""

    @staticmethod
    def main():
        bugs =BugsMusic()
        while 1:
            menu= int(input('0.Exit\n 1.Input URL \n 2.Get Ranking'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('Input URL')
            elif menu == 2:
                print(f'Input URL is {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')

                bugs.scrap(soup)



            else:
                print('Wrong Number')
                continue

BugsMusic.main()