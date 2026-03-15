class Company:
    def __init__ (self,company_name):
        self.company_name = company_name

    def company_info(self):
        return (self.company_name)  
    
    def location(self):
        return "pude(mumbai)"

class emp(Company):
    def __init__ (self,company_name,emp_name,sallary):    
          super(). __init__ (company_name)
          self.emp_name = emp_name
          self.sallary = sallary

    def emp_info(self):
        return "BCA from RMS foundation"

    def emp_intro(self):
        print(f"I am {self.emp_name} from Bhanpura and i have compeleted {self.emp_info()} . and i am working in {self.company_name} .And my sallary is {self.sallary} ") 

e1 = emp("TCS","Aarav-Rathore",50000)
e1.emp_intro()