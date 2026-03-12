class Student():
    x = 10
    def __init__ (self,Name,Age,Roll_no,marks):
        self.name = Name
        self.age = Age
        self.roll_nu = Roll_no
        self.marks = marks

    def about(self):
        print(self.age)

S1 = Student("Ayan",12,1011,92)
print(S1.name)
print(S1.age)
print(S1.roll_nu)
print(S1.age)
