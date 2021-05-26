class Vector_test(object):
    def __init__(self):
        pass


    @staticmethod
    def main():
        ls = ['abcd', 786, 2.23, 'john', 70.2]
        tinyls = [123, 'john']
        v = Vector_test()
        while 1:
            menu = input('0.EXIT 1.CREATE 2.READ 3.UPDATE 4.DELETE')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(100)

            elif menu == '2':
                print(ls)

            else:
                continue

Vector_test.main()

