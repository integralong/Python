#Week 8 Lecture 2

#recap lambda function(using ternary conditional form and default parameters)
##minval = lambda a = 1, b = 2: a if a <= b else b
##
##n1, n2 = input('Enter two numbers (separated by a space): ').split()
##n1, n2 = float(n1), float(n2)
##print(f'The smaller value is {minval(n1,n2)}')
##print(f'The smaller value is {minval(n1)}')
##print(f'The smaller value is {minval()}')

#-----more about types-----
#string slicing
##name = 'Schinnel Small'
##subname = name[5: 11] #starting position it 5(incl.); ending position is exclusive
#position 5 to 10 -> output: nel Sm
##print(subname)

#you can use = vd indices to create a substring
##subname2 = name[-5: -2]
##print(subname2)

#you can omit starting and ending values too
##subname3 = name[4:]
##print(subname3)
##
##subname4 = name[: -3]
##print(subname4)

#See section 7.3 and 8.2 for String and limit methods



#list comprehension - create a new list by accessing an orginal list
list1 = [1, 2, 3, 4, 5] #original list
list2 = [i * 10 for i in list1]

print(list1)
print(list2)



#you can use limit comprehension with the ternary form
list3 = [m / 2 if m > 3 else m * 2 for m in list1]#ternary form is first
print(list3)


#you can use limit comprehension with an if statement
list4 = [n - 1 for n in list1 if n <= 2] #if statement is last
print(list4)

#you can list comprehension with input...but use carefully
list5 = [(float(input('value'))) for p in list1]
print(list5)


#dictionary comprehension - quick way to create a dictionary
test = {n: n ** 2 for n in range(10)}
print(test)

print(test[7])




























