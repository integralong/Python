#Class file - Bank Account

class BankAccount:
    def __init__(self, n, ac, b):
        self.__name = n
        self.__accountnumber = ac
        self.__ballance = b

    #accessors
    def getname(self):
        return self.__name

    def getaccountnumber(self):
        return self.__accountnumber

    def getballance(self):
        return self.__ballance


    #mutators
    def setname(self, n):
        self.__name = n

    def setaccountnumber(self, ac):
        self.__accountnumber = ac

    #methods to adjust balance
    def deposit(self, amt):
        self.__balance += amt
        
    def withdraw(self, amt):
        if self.__balanve >= amt:
           self.__balanve -= amt:
            
        else:
            print('Insufficient balance')
            
    
        
    
    

