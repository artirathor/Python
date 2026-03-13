class Person:
    def __init__ (self, firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname 
        self.age = age 

    def detail(self):
        return f"My name is {self.firstname} {self.lastname}, from Sandalpur"

    def about(self):
        print(self.detail() ,"and i have compeleted BCA from RMS foundation.")
        pass 

class Student(Person):
    pass
    
s1 = Student("Arti","rathore",4)
s1.about()    


