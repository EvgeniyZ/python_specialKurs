import random
import os
import sys

class Animal:
    def __init__(self, name, info):
      pass
        
class Mammal(Animal):
    def __init__(self, kind):
      self.kind = kind


class Lion(Mammal):
    def __init__(self, name, info):
      self.name = name
      self.info = info
    def __str__(self):
      return "Animal in this cage : {0}".format(self.name)   
    def showinfo(self):  
      return "{0}".format(self.info)
        

def createzoo:
    zoo = {'млекопитающие':Lion(input(name), input(info))
            }
    zoo = {}
    l = Lion()
    zoo[l.kind] = l
    
        
def main():
    

if __name__ == '__main__':
    main()
