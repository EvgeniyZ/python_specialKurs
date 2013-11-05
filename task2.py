import random
import os


def main():
    def watch(l, name, namefile):
        if not l:
            placein(name, namefile)
        else:
            for line in l:
                if (name == line.rstrip()):
                    print("Такое имя уже есть")
                    name1 = name + str(random.randint(0, 100000))
                    name2 = name + str(random.randint(0, 100000))
                    name3 = name + str(random.randint(0, 100000))
                    name4 = name + str(random.randint(0, 100000))
                    print("Возможные варианты регистрации: ", name1,
                          '\n', name2, '\n', name3, '\n', name4)
                    nameuse = input("Введите одно из этих похожих имен")
                    watchout(l, nameuse, namefile)

    def watchout(l, nameuse, namefile):
        for line in l:
            if (nameuse == line.rstrip()):
                print("Вы повторили неправильный ввод, попробуйте еще раз")
                name = input("Введите имя")
                watchout(l, name, namefile)
            else:
                placein(nameuse, namefile)

    def placein(nameuse, namefile):
        print("вы ввели удачное имя")
        fp = open('/home/student/python_specialKurs/' + namefile,
                  'a+')
        fp.write(nameuse + '\n')
        fp.close()

    def register(name):
        namefile = input("Введите имя файла")
        if os.path.exists('/home/student/python_specialKurs/' + namefile):
            fp = open('/home/student/python_specialKurs/' + namefile)
            l = [line.strip() for line in fp]
            else:
                fp = open('/home/student/python_specialKurs/' + namefile,
                          'x')
                l = []
        fp.close()
        watch(l, name, namefile)
    name = input("Введите имя")
    register(name)


if __name__ == '__main__':
    main()
