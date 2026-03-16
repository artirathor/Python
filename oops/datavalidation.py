class SBI_account:
    def __init__(self, Balance):
        self.__Balance = Balance

    def deposite(self, amount):
        if amount > 0:
            self.__Balance = self.__Balance + amount
            print("deposit successfully")
        else:
            print("invalid amount")

    def get_balance(self):
        return self.__Balance


acc = SBI_account(5000)

acc.deposite(4000)
print(acc.get_balance())