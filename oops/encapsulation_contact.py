class person:
    def __init__ (self,email,mo_number):
        self.email = email
        self.__mo_number = mo_number

    def get_mo_number(self):
        return self.__mo_number

    def contact(self):
        print(f"mobile number : {self.get_mo_number()} Email : {self.email}")   

p = person("ArtiRathor2022@gmial.com",9302292328)
p.contact()
