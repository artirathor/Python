class Animal:
    def __init__ (self):
        pass

class Dog(Animal):
    def sound(self):
        print("dog barks")

class Cat(Animal):
    def sound(self):
        print("cat myauuu")

class Duck(Animal):
    def sound(self):
        print("ducks quacks")
        
class Lion:
    def sound(self):
        print("lions roar")

D1 = Dog() 
c1 = Cat()
l1 = Lion()
d1 = Duck()

D1.sound() 
c1.sound()    
l1.sound()    
d1.sound()    
        

