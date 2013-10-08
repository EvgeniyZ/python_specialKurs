import random

def main () :
    def register(name) :
        fp = open (base,'+')        
        for line in fp :            
            if name == line :
                print("Такое имя уже есть")
                t = t + random.choice()
                fp.close()
                fp = open ()
            else :
                fp.write(name)
    print("Введите имя")        
    try :
        name = string (input())
    except TypeError:
        print("неккоректный ввод")
    else :
         register(name)   
   
if __name__=='__main__' :
    main ()
