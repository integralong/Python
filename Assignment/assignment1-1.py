#Lauren Song
#U79789182
#Value Swap

num1 = int(input('Please enter your first integer:'))
num2 = int(input('Please enter your second integer:'))

print('The values in num1 and num2 before the swap are:')
print('num1=',num1,'and num2=',num2)

num1 = (num1 + num2)
num2 = (num1 - num2)
num1 = (num1 - num2)

print('The values in num1 and num2 after the swap are:')
print('num1=',num1,'and num2=',num2)
