from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls =[]
    artist_ls = []
    dict = {}

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------- 제목 --------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[1]}))
        for i in ls:
            print(f' {i.find("a").text}')
            self.title_ls.append(i.find("a").text)
        print('------ 가수 --------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls:
            print(f'{i.find("a").text}')
            self.artist_ls.append(i.find("a").text)

    def insert_title_dict(self):
        for i,j in self.title_ls:
            self.dict[j] = self.artist_ls[i]
        print(self.dict)
        #제목을 key 로 가수를 value 로

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input time, 2-output 3-input title with dict')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url(input('상세정보 입력')) # wl_ref=M_contents_03_01
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()

            elif menu == '3':
                #bugs.title_dict[insert_title_dict.ls] = insert_title_dict.ls2
                bugs.insert_title_dict()

            else:
                print('Wrong Number')
                continue

BugsMusic.main()


