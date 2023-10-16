#Week 5 Lecture 1

#Types: string, list, tuple, sets, dictionaries (intro to chapter 3 in zyBook)

#strings: sequence type (contents have order), use index to access specific value
name = "Cloud strife" # first position is 0; last position is -1
print(name)
print(name[-1])


#strings are immutable

#name[2] = 'X' #does not work
name = "Tifa Lockheart" #changing a reference to name
print(name)

#len function - to obtain the size of a string/list
print(f'The name {name} has {len(name)} characters.')

#Lists - containers (structure that can hole different types of data)
#and sequences
items = ['cheese', 'eggs', 2, 5.6, 'oragne juice']
print(items)
print(items[1])
print(items[1][0])

#lists are mutable(변하기쉬운)
items[-2] = 'milk'
print(items)

#methods: append, pop, remove
items.append('bacon')
print(items)

items.pop() #pop removes a value at the end of a list(default)
print(items)

items.pop(2) #can remove a valuebased position 번호는 순서의 번
print(items)

items.remove('eggs')
print(items)


#turple - sequence, containers
something = (1,'A', "spam", 5.4)
print(something)
print(something[2])

#someting[1] = 'B'

#tuple with 1 value
constant = (95,)#insert a comma
print(constant)
constant = 89
print(constant)


#sets: table 3.5.1, 3.5.2 for common set oparations
#sets: containers, but they are not sequence
s1 = {4, 5, 2, 'six', 1, 3, 4, 2}
#print(s1[4]) gives error
print(s1)

s1.add(6.0)
s1.remove('six')

print(s1)

#---intro to dictionaries---
#dictionaries are containers (used for associative relationships)
#mapping type: key value pair
di = {'cat':'floof'}

#use the key to access the value
print(di['cat'])

scores = {'Annie': [92,97], 'Brad': [91,98]}
print(scores['Annie'][1])




