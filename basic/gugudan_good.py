"""
구구단 프로그램은 단을 입력받아서, 입력받은 단의 1~9의 곱을 출력하는 어플이다.
단, 단은 정수이다. dan = 0
(단은 실수이다. dan = 0.0)
파라미터 쓰는 것 후진적인 코드, 인공지능 코드에 파라미터 거의 없음
<----
dan = 0
def abc(self):
pass ---> 기본구조
"""

class Gugudan(object):
    dan = 0

    def calc(self):
        for i in range(1,10):
            print(f'{self.dan} * {i} = {self.dan * i}')

    @staticmethod
    def main():
        gugudan = Gugudan()
        while 1:
            menu = input('0-exit 1-input dan')
            if menu == '1':
                gugudan.dan = int(input('단 입력'))
                gugudan.calc()
Gugudan.main()