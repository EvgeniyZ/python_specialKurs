import random
import os
def main():
    def register(name):
        namefile = input("Введите имя файла")
        if os.path.getsize('/home/student/python_specialKurs/'
                           + namefile) == 0:
            print("пишем в пустой файл!")
            fp = open('/home/student/python_specialKurs/' + namefile, 'w')
            fp.write(name + '\n')
            fp.close()
        else:
            fp = open('/home/student/python_specialKurs/' + namefile, 'r')
            for line in fp:
                if (name == line.rstrip()):
                    print("Такое имя уже есть")
                    name1 = name + str(random.randint(0, 100000))
                    name2 = name + str(random.randint(0, 100000))
                    name3 = name + str(random.randint(0, 100000))
                    name4 = name + str(random.randint(0, 100000))
                    print("Возможные варианты регистрации: ", name1,
                          '\n', name2, '\n', name3, '\n', name4)
                    try:
                        nameuse =
                        str(input
                            ("Введите одно из этих похожих имен"))
                    except TypeError:
                        print("неккоректный ввод")
                    fp.close()
                    fp = open
                    ('/home/student/python_specialKurs/' + namefile, 'w')
                    fp.write(nameuse + '\n')
                    fp.close()
                    break
            else:
                print("вы ввели удачное имя")
                fp.close()
                fp = open('/home/student/python_specialKurs/' + namefile, 'w')
                fp.write(name + '\n')
                fp.close()
    try:
        name = input("Введите имя")
    except TypeError:
        print("неккоректный ввод")
  
    else:
        register(name)   
   
if __name__=='__main__' :
    main ()
