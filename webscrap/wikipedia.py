class Wikipedia(object):
    def __init__(self, url):
        self.url = url

    def to_string(self, url):
        return self.url

    @staticmethod
    def main():
        wiki = Wikipedia
        while 1:
            menu= int(input ('0.EXIT\n 1.INPUT\n 2.PRINT URL'))
            if menu == 0:
                break
            elif menu == 1:
                wiki = Wikipedia(input('Input URL'))
            elif menu == 2:
                print(f'{wiki}')
            else:
                continue

Wikipedia.main()