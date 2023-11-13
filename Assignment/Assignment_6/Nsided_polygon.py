#Lauren Song
#U79789182
#N-sided Polygon class definition and main function
import math

class Polygon:
    def __init__(self):
        self.numsides = 0
        self.length = 0.0

    #accessors
        
    def getsides(self):
        return self.numsides
    
    def getlength(self):
        return self.length

    #mutators

    def setsides(self, n):
        if n >= 3:
            self.numsides = n
        else:
            print('Invalid entry. Re-entry the number of sides(>=3):')
        
    def setlength(self, s):
        if s >= 0.1:
            self.length = s
        else:
            print('Invalid entry. Re-entry the length of each sides(>=0.1):')

    #classmethod

    @classmethod
    def get_perimeter(cls, numsides, length):
        return numsides * length
    
    @classmethod
    def get_area(cls, numsides, length):
        return (numsides * (length ** 2)) / (4 * math.tan(math.pi / numsides))

def main():
    polygon = Polygon()

    numsides = int(input('Enter the number of sides(>=3):'))
    while numsides < 4:
        numsides = int(input('Invalid entry. Re-entry the number of sides(>=3):'))
    length = float(input('Enter the length of each sides(>=0.1):'))
    while length < 0.1:
        length = float(input('Invalid entry. Re-entry the length of each sides(>=0.1):'))

    polygon.setsides(numsides)
    polygon.setlength(length)

    print(f'The polygon has {polygon.getsides()} sides. Each side is {polygon.getlength()} units in length.')
    perimeter = Polygon.get_perimeter(polygon.getsides(), polygon.getlength())
    area = Polygon.get_area(polygon.getsides(), polygon.getlength())
    print(f'The perimeter of the polygon is {perimeter:.3f} units and its area is {area:.3f} squre units.')


if __name__ == "__main__":
    main()
    
                   

