def main () :
    def f(t) :       
        if t < -273 or t >= 6000 :
            print("плохо ввел температуру")         
        else :
            kelvin = t + 273
            print ("KELVIN:",round(kelvin,2))            
            fahrenheit = t*9/5 + 32
            print ("CELCIUS:",round(fahrenheit,2))
          
    print("Что будем переводить?")
    try :
        t = float (input())
    except ValueError:
        print("неккоректный ввод")
    else :
         f(t)   
   
if __name__=='__main__' :
    main ()
    
