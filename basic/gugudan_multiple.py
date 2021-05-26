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
    dan2 = 0

    def gugudan(self):
        print(self.dan * self.dan2)


    @staticmethod
    def main():
        g = Gugudan()
        menu = input('0.EXIT 1.MULTIPLE')
        while 1:
            if menu == '0':
                break

            elif menu == '1':
                g.dan = int(input('첫번째 숫자입력'))
                g.dan2 = int(input('두번째 숫자입력'))
                g.gugudan()

            else:
                continue

Gugudan.main()




