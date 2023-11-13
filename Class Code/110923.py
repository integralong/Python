#Week 12 Lecutre 2

#Multiple Inheritance Example

###parent classess
##class Animal:
##    def __init__(self, name):
##        print(f'{name} is an animal.')
##        #super().__init__(name)
##        
##class CannotFly:
##    def __init__(self, name):
##        print(f'{name} cannot fly.')
##        super().__init__(name)
##
##class LikestoHunt:
##    def __init__(self, name):
##        print(f'{name} likes to hunt')
##        super().__init__(name)
##
###child class
##class Cat(LikestoHunt, CannotFly, Animal):
##    def __init__(self, name):
##        print(f"I'm a cat named {name}.")
##        super().__init__(name)
##    

###main portion
##kitty = Cat('Pandemica')
##
###protected status for attributes
##class Shape:
##    def __init__(self, l, w):
##        self._length = l # _ means attribute is protected
##        self._width = w
##
##
##    def __str__(self):
##        return f'Length: {self._length}, Width: {self._width}'
##
##class Rectangle(Shape):
##    def __init__(self, l, w):
##        Shape.__init__(self, l, w)
##        self._color = 'red'
##
##    def setlength(self, l):
##        self._length = l
##        
##    def setwidth(self, w):
##        self._width = w
##
##    def area(self):
##        print(f'Area is {self._length * self._width}')
##
###main portion
##r = Rectangle(80, 20)
##r.area()
##print(r)
##
##s = Shape(10, 20)
##print(s)

#All about polymorphism (many forms)
#Example 1 - polymorphism in built in functions
print(len('3 more weeks!'))
print(len([10, 34, 56, 78, 90]))

#Example 2 - polymorphism in programmer - defined funtions
def add(x, y, z=0):
    return x + y + z

print(add(2, 3))
print(add(2, 3, 4))

#Example 3 - polymorphism in classes (via methods)


#Example 4 - polymorphism in inheritance


