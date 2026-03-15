class Vehicle:
    x = 30
    def __init__ (self, modal,colur):
        self.modal = modal
        self.colour = colur

class Car(Vehicle):  
    def move(self):
        print("Drive")

class Boat(Vehicle): 
    def move(self):
        print("Sail")  

class Aroplane(Vehicle): 
    def move(self):
        print("Fly") 
c1 = Car("jai299","red")       
b1 = Boat("xyz","blue")
a1 = Aroplane("abc","white")

for x in (c1,b1,a1):
    (x.move())
    print(x.modal)
    print(x.colour)
