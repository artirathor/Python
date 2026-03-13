class College:
    def __init__ (self,name):
        self.name = name

    def __str__(self):
        return ("hello python " + self.name)

c1 = College("arti")     
print(c1)   

