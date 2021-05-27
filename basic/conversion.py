class Conversion(object):
    inn = 0
    f = 0.0
    s = ''
    ls = []
    tp = ()
    dict = {}

    def one(self):
        self.tp = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        return self.tp

    # return은 저장하지 않고 일회용으로 쓰고 버려라 코드

    """
    def two(self):
        for i,j in enumerate(self.tp):
            self.ls.append(i)
        return self.ls
    """

    def two(self):
        self.ls = [j for i, j in enumerate(self.tp)]
        return self.ls

    def three(self):
        for i, j in enumerate(self.ls):
            self.f = j
        return self.f

    def four(self):
        self.inn = int(self.f)
        return self.inn

    def five(self):
        for i, j in enumerate(self.inn):
            self.dict = {str(i): j}
        return self.dict

    def six(self):
        pass

    def seven(self):
        pass

    @staticmethod
    def main():
        c = Conversion()
        while 1:
            m = input('0-exit 1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list')
            if m == '0':
                break
            # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)

            elif m == '1':
                print(c.one())

            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '2':
                print(c.two())

            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '3':
                print(c.three())

            # 3번 실수(float) 리스트를, 정수 리스트로 바꾸시오  (return)
            elif m == '4':
                print(c.four())

            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '5':
                print(c.five())

            # 'hello' 를 튜플로 전환하시오
            elif m == '6':
                print(c.six())

            # 6번 튜플을 리스트로 전환하시오
            elif m == '7':
                print(c.seven())
            else:
                continue


Conversion.main()