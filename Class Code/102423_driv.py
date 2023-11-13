#Driver file -  Transactions

from BankAccount import BankAccount #from [module] import [class]
acct1 = BankAccount('John Doe', 10001, 1000)

print(f'At Kitosk 1: An account for {acct1.getname()} was created.')

print(acct1)

print('At Kiosk 2')
name = input('Enter a name:')
acctnum = int(input('Establish an accoint number:'))
startbal = float(input('Enter a starting balance:'))

#create another object
acct2 = BankAccount(name, acctnum, startbal)

print('Back at Kiosk 1')
dep = float(input(f'How much to deposit to account {acct1.getaccountnumber()}?'))
acct1.deposit(dep)

print(acct1)
print(acct2)
