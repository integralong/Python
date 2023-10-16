#Week 3 Lecure 1

#---multiple input---
#option 1: mulitple input statements, (with a print prompt)
##print("Enter 2 values(integer followed by floating point):")
##a = int(input())
##b = float(input())
##f = a + b
##print(f)
##
##print(f'The values entered were {a} and {b}')
##
###option 2- read all input as a string, then convert as needed
##c,d = input('Enter another 2 values (int and float) separated by space:').split()
##print(f'The values entered were {c} and {d}')
###c = int(c)
###d = float(d)
##e = (c) + float(d)
##print(e)

#walrus operator
g = 7
print('g is now', g:=7.8)#:= allows assignment and printing

print(f'g is now {g :=10}') #walrus operator has varying effects with f string

#walrus operator with input 
print('h is ', h := int(input('Enter an integer:'))) #it works, just need more ()
print(f'h is {(h := int(input("Enter an integer:")))}') #it works but NO

#compund assignment

##g = g + 4 #update 
##g += 4 #g = g + (4)
##g*= 7 + y #g = g * (7 + y)



