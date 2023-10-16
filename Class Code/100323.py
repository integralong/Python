#Week 7 Lecture 1
    
a = 15 #global variable (defined outside of a function or block) (bad idea)
MAX = 50 #global 'constant' - great idea


def main():
    a = 5 #local variable (defined inside of a function or block)
    print(f'In main: a is {a}')
    fun1(a)#this a is argument
    fun2(a)
    fun3()
    print(f'In main: a is {a}')
    print(f'In main: MAX is {MAX}')


    #funtions parameter/arguments can be any object
    list1 = [1, 2, 3, 4, 5, 'six']
    printlist(list1)

#main() (this location gets error)

#a = 15 (still works)
   
def fun1(x): #x is local to fun1, recives copy of value in local a from main (5)
    print(f'In fun1: a is {x}')
    print(f'In fun1: a is {a}') #{a}is parameter ex.x in fun1(x) -> parameter?


def fun2(a): #a is local to fun2, reveives copy of value in local a from main (5)
    a += 7 #a = a + (7) = 5 + 7 = 12
    print(f'In fun2: a is {a}')
    return #not necessary #why return keyword is unecessary??

def fun3():
    print(f'In fun3: a is {a}')

def printlist(l): #l is a list parameter
    for (i,e) in enumerate(l):
        print(f'Index: {i}, Element: {e}.')
    





#-----no definitions below this line-----
main()

#a = 15 (error)
