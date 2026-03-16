class SBI_bank:
    def __init__ (self,candidate_name,account_no):
        self.candidate_name = candidate_name
        self.__account_no = account_no
        
sb = SBI_bank ("Aaru Rathore",654373228)
print(sb.candidate_name)
print(sb.__account_no)
