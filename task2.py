import random

def main () :
    def register(name) :
        fp = open ('/home/student/python_specialKurs/testing.txt','r')     
        l = open('/home/student/python_specialKurs/testing.txt').readlines()
        fp.close
        if name in l :                
            print("Такое имя уже есть")
            name1 = name + random.choice()
            name2 = name + random.choice()
            name3 = name + random.choice()
            name4 = name + random.choice()
            print("Возможные варианты регистрации :",name1,'\n',name2,'\n',
                      name3,'\n',name4)            
            try :
                nameuse = str(input("Введите одно из этих похожих имен, или новое имя"))
            except TypeError:
                print("неккоректный ввод")          
            fp = open ('/home/student/python_specialKurs/testing.txt','a')
            fp.write(nameuse + '\n')
            fp.close()
        else :
            fp = open ('/home/student/python_specialKurs/testing.txt','a')
            fp.write(name + '\n')
            fp.close()          
    try :
        name = str(input("Введите имя"))
    except TypeError:
        print("неккоректный ввод")
  
    else :
         register(name)   
   
if __name__=='__main__' :
    main ()
