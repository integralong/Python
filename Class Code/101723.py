#Week 9 Lecture 1

###File i/o
dogfile = open('popularbreedsUS.txt', 'r') #r - read mode
breeds = dogfile.readlines() #readlines - read contents and return a list
##dogfile.close()
##print(breeds)


#alternate use with, as keywords
##with open('popularbreedsUS.txt', 'r') as dogfile:
##    db = dogfile.read() #read - read contents and reutrn a string
##    db2 = dogfile.readline() #readline - read contents one line at a time
##
##print(db)   
##print(db2)

#clean up list
dogs = []
for b in breeds:
    d = b.rstrip()
    dogs.append(d)
print(dogs) #print(dogs[56]) -> Whippets


###to write to a file
###w - write mode; a - append; r+ w+ reprent updates
##with open('sentence.txt', 'w') as outfile:
##    outfile.write('Confirm plans for Thanksgiving.') #check the file named sentence.txt#
##    
###echo print to see contents of breeds
##
##
##
###Matplotlib
###pip3 install matplotlib
##import matplotlib.pyplot as plt



###E.g.1 - use small list
##x = [10, 20, 30, 40]
##y = [20, 35, 55, 75]
##
##plt.plot(x,y) #draw the plot#
##plt.grid(True) #draw the grid#
##
##plt.show()
##
##
###E.g.2 - import a file
##with open('gltmarch.csv', encoding = 'utf-8-sig') as tempfile:
##    gtemps = []
##    for g in tempfile:
##        gtemps.append(float(g))
##
##
##years = range(1900, 2016)
##plt.plot(years, gtemps)
##plt.xlabel('Year')
##plt.ylabel('Global Temps (F)')
##plt.title('Global Temperatures in March from March 1900 to March 2015')
##plt.show()
##














