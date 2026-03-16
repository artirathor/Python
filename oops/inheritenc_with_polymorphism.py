class Animal:
    def __init__ (self,name,age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__ (self,name,age,colour):
        super(). __init__ (name,age)    
        self.age = age
        self.colour = colour

    def sound(self):
        print("dog barks")

class Lion(Animal):
    pass

    def sound(self):
        print("lion roars")

class Duck(Animal):
    pass

    def sound(self):
        print("duck squaks")

d1 = Dog("puppy,",6,"black")
l1 = Lion("ahersing",13)
D1 = Duck("kuku",2)

for x in (d1,l1,D1):
    x.sound()