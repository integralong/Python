#week 1 lecture
#--used for comment--
##Name
##U-Number
##Brief Description

'''This can be used
for multi-line comments'''

print('I can not wait for November')

print('I can\'t wait for November') #\escape sequence

print("I can't wait for November")

print() #printing a skipped line due to end='\n'                       

print('I said \"Hello\" to you.') #\"prints the"

print('\n') #printing two skipped lines due to string and end='\n' 

print('"Pumpkin Spice" season is almost there')

print('''A Florida woman was arrested after she hit the wrong man with a burrito.
She intended to hit a man with whome she was arguing but didn't hit her target.
The burruto "hit the vicitm in the face" according to the affidavit.''')

print(3,end = '...')
print(2,end = '...')
print(1,end = '...')

print('sksmall','usf.edu', sep = '@')

#---------------------------------------------------------------------------

###week 2 lecture
###---variables and f-stirngs---
#var = 45 #var-variable, = is the assignment operator, 45 indicates literal and type of value
##
###echo printing
##print('var is', var)#printing a variable (old way)
##print(f'var is {var}')#printing with an f-string; {} tells the interpreter to print content of a variable
##
###zybooks 2.2 identifiers
####
#####update variable with hardcoding
####var = var + 9
####print(f'var is {var}')#var = 45 +9 = 54
##
###---input---
##var2 = input()#no prompt (i.e. no msg to let the user know that input is needed)
###devault value for the input fuction is a string
#int - converts strings to int
#float - convert strings to float

##var2 = float(input('Enter a number:'))
##print(f'var2 is {var2}') #echo printing for var2
##
##result = var2 - var
##print(f'result is {result}') #echo printing for result


#Math operations: +, -, *, /, //, %, **
# / - floating point division
# // - integer division
# % - remember operator



#Operation precedence (see section 2.4, 2.5 in zyBooks)



#---enotation---

jackpot = 1.58e9 #e(scientific notation)
print(f'A ticket sold in Florida has won the ${jackpot} Megamillions jackpot.')
print(f'A ticket sold in Florida has won the ${jackpot:.2f} Megamillions jackpot.')#applying format using:.2f
print(f'A ticket sold in Florida has won the ${jackpot:,.2f} Megamillions jackpot.')#same, but with comma separation

























