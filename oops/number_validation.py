class Person:
    def __init__(self,name,Mo_number):
        self.name = name
        self.__Mo_number = str(Mo_number)

    def validation(self):
        if len(self.__Mo_number) == 10:
            print("valid number")
        else:
            print("invalid number")        

    def get_Mo_number(self):
        return self.__Mo_number

p = Person("Arti",9302292328)         
print(p.get_Mo_number())   
p.validation()