class Animal:
    x = 10

    def __init__ (self,Name):
        self.name = Name

    def speak(self):
        return (self.name)

class Dog(Animal):
    def __init__ (self ,Name,Age):
        super(). __init__ (Name)
        self.age = Age

    def sound(self):
        print(f"hello ,this is name: {self.speak()},and it is {self.age} years old.")    

d1 = Dog("rex",5)
d1.sound()
