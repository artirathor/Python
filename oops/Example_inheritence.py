class Person:
    def __init__ (self,fname,lname):
        self.fname = fname
        self.lname = lname

    def show(self):
        print(f"my name is {self.fname} {self.lname}")

class Student(Person):
    def __init__ (self,fname,lname,age):
        super().__init__ (fname,lname)
        self.age = age 

    def show(self):
        print(f"my name is {self.fname} {self.lname} age : {self.age}")

s1 = Student("Arti","Rathore",30)
s1.show()        
