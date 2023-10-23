#Week 9 Lecture 2

###A little more on matplotlib
##from matplotlib import pyplot as plt
##import numpy as np
##
##
###create equally spaced data in range 0 to 2*pi (100 poijnts)
##theta = np.linspace(0, 2*np.pi,100)
##
###generate x and y data using formula
##x = 16 * (np.sin(theta) ** 3)
##y = 13 * np.cos(theta) - 5 * np.cos(2 * theta) -2 * np.cos(3 * theta) - np.cos(4 * theta)
##
##
###plot the graph
##plt.plot(x, y, 'r')
##plt.title('Heart shape')
##plt.fill(x, y, 'r')
##plt.show()

#Intro to classes!
#object - entity that has both data (data, attributes) and beahvior (methods)
#class - recipe (blueprint) for objects; they define what your obeject is

#how (not) to create a  class
##class Test:
##    pass #place holder for meaningful code
##
###create object
##test1 = Test()
##print(test1) #shows memory address of a Test object
##
###can create attributes, but outside of the class
##test1.name = 'Programming Exam2'
##print(f'{test1.name} is on Thursday Oct. 26th.')


#better way to create a class
class Television:
    #initilizer method - call automatically when an object is created
    def __init__(self):#self - placeholder for object
        self.__channel = 1 #__ introduces level of privacy
        self.__volume = 1 
        
    #accessor (getter) methods
    def getchannel(self):
        return self._channel
    
    #mutator (setter) methods
    def setchannel(self, ch):
        self.__channel = ch
        
    #str (string) method
    def __str__(self): #call automatically when an object is passed through a print function
        return f'TV stats: \nChannel: {self.__channel}\nVolume: {self.__volume}'

#end Television class
    

def main():
    #create object
    tv1 = Television() #call__init__

    print(tv1)

    #test mutator
    tv1.setchannel(58)
    
    print(tv1)

#end main function

#call to main

main()
























