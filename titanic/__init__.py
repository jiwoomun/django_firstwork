from titanic.views.controller import Controller



if __name__ == '__main__':
    controller = Controller()
    #인스턴스만

    while 1 :
        menu = input('0-exit \n 1-preprocess')
        if menu == '0':
            break

        elif menu == '1':
            controller.preprocess('train.csv')

        else:
            continue

