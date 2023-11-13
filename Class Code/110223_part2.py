#Week 11 Lecture 2 Part 2

#Topic: Intro to inheritance

#---Class definitions---
#parent(or super, base) class
class Vehicle:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        
    def getmake(self):
        return self.__make

    def getmodel(self):
        return self.__model

    def getyear(self):
        return self.__year

#end parent class
        
#child (or sub, derived) class
class Car(Vehicle): #establish inheritance by putting parent class in ()
    def __init__(self, make, model, year, ndoors):
        #explicitly call parent class's init method
        #Vehicle.__init__(self, make, model, year)

        #call the parent clas again using the super reference
        super().__init__(make, model, year)
        
        #set up additional attributes(specific to Car object)
        self.__ndoors = ndoors
    def getnumdoors(self):
        return self.__ndoors
    
class ElectricCar(Car):
    pass
    


        
    
#end class definitions

#---driver portion---#
#create vehicle object
ve1 = Vehicle('Hyundai', 'Elantra', 2023)
print(f'My brother drives a {ve1.getyear()} {ve1.getmake()} {ve1.getmodel()}.')


#create vehicle object
car1 = Car('Honda', 'Accord', 2022, 4)
print(f'My friend drives a {car1.getnumdoors()}-door {car1.getyear()} {car1.getmake()} {car1.getmodel()}.')


