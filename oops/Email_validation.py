class Person:
    def __init__(self,name,email):
        self.name = name
        self.__email = email

    def validatiom(self):
        if "@" is self.__email and "." in self.__email:
            print("Valid email")
        else:
            print("Invalid email")    

    def get_email(self):
        return self.__email
E = Person('arti',"artirathor2022@gmail.com")   
print(E.get_email())
print(E.name)
print(f"my name is {E.name} and my email id: {E.get_email()}.")

