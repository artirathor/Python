class Bank:
    def __init__(self,balance,acc_num,passwrd):
    
        self.balance = balance
        self.acc_num = acc_num
        self.__passwrd = passwrd

    def deposite(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposit successful! Current balance: {self.balance}")


        else:
            ("insuffsient balance")

    def get_passwrd(self):
        return self.__passwrd

b = Bank(1000,9325233221,"AAru@234")    
b.deposite(3000)
print(b.balance)
print(b.get_passwrd())
          
