###Note: This ppart is from last week's lecture
###All about polymorphism (many forms)
###Example 1 - polymorphism in built in functions
##print(len('3 more weeks!'))
##print(len([10, 34, 56, 78, 90]))
##
###Example 2 - polymorphism in programmer - defined funtions
##def add(x, y, z=0):
##    return x + y + z
##
##print(add(2, 3))
##print(add(2, 3, 4))
##
###Example 3 - polymorphism in classes (via methods)
##class Canada:
##    def capital(self):
##        print('Ottowa is the capital of Canada.')
##    def language(self):
##        print('The official languages of Canada are French and English.')
##        
##class USA:
##    def capital(self):
##        print('Washington DC is the capital of U.S.A.')
##    def language(self):
##        print('The official language of U.S.A English.')
        
##
##canada = Canada()
##usa = USA()
##
##for country in (canada, usa):
##    country.capital()
##    country.language()
##
##
###Example 4 - polymorphism in inheritance
##class Bird:
##    def intro(self):
##        print('There are many types of birds.')
##
##    def flight(self):
##        print('Some birds can fly, while other cannot.')
##        
##class Robin(Bird):
##    def flight(self):
##        print('Robins can fly.')
##        
##class Ostrich(Bird):
##    def flight(self): #attached below:
#method overriding - when a method from a child class defines a method
#method
##        print('Ostriches cannot fly.')
##
##bird = Bird()
##rob = Robin()
##ost = Ostrich()
##
##bird.intro()
##bird.flight()
##
##rob.intro()
##rob.flight()

##ost.intro()
##ost.flight()


#Exceptions - errors that can be reasonably handled
#Not every error in an exception!
#value1 = int(input('Enter numerator:')) -> if put q -> its ouptput value error

#**********#
#try block - insert code where an exception can occur
try:
    value1 = int(input('Enter numerator:'))
    value2 = int(input('Enter denominator:'))


    ans = value1 / value2

#except block - area where the error is handled
##except ValueError:
##    print('Wrong value entered: integer expected')


except ZeroDivisionError as msg:
    print(msg)


except: #generic block
    print('Some other error has occured') 
    
else:
    print(f'{value1} / {value2} = {ans}')


finally: #optional - block runs regardless of error
    print('Done with this code.')















    












