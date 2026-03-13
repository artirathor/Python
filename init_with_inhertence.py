class Person:
    def __init__ (self,fname,lname):
        self.fname = fname
        self.lname = lname

    def show(self):
        print(f"{self.fname} {self.lname}") 

class Student(Person):
    def __init__ (self,fname,lname,):
        Person. __init__ (self,fname,lname)


s1 = Student("Arti","rathore")
s1.show()




