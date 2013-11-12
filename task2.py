import random
import os
import sys


def main():
    def watch(l, name, namefile):
        flag = 1
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
                    flag = 0
            if(flag == 0):
                watch(l, nameuse, namefile)
            else:
                placein(name, namefile)

    def placein(nameuse, namefile):
        print("вы ввели удачное имя")
        fp = open('/home/student/python_specialKurs/' + namefile,
                  'a+')
        fp.write(nameuse + '\n')
        fp.close()

    def register(name):
        if (len(sys.argv) > 1):
            namefile = sys.argv[1]
        else:
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
