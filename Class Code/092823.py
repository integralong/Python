#COP 2510 Week 6 Lecture 2
#Introduction to fuctions

#-----functions definitions-----
def main(): #function header
    x = int(input('Enter a value:'))
    print(f'In main function: The value of x is {x}.')

##    y = quadval(x) #function call with x as an argument
##    print(f'In main function: The value of y is {y}.')
    print(f'In main function: The quadrupled value is {quadval(x)}.')


    changeto89(x)
    print(f'In main function: The value of x is {quadval(x)}.')

#with duplicate functions, python refers to the most recent version
##def main():
##    print('This is the second main function')
##
##def main():
##    print('This is the third main function')

#calue returning function(accpet and return a value)
def quadval(val):
    print(f'In quadval, the value accpeted was {val}.')
    val *= 4
    print(f'In quadval, the value returned is {val}.')
    return val

#void function (accept a value)
def changeto89(var):
    print(f'In changeto89, the value accpeted was {var}.')
    var = 89
    print(f'In changeto89, the value is now {var}.')


#-----no definitions below this line-----
#functions must be called 
#main() #call to main

import wk6test

