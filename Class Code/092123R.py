# Week 5 reward point system

number = int(input("Enter the number of books:"))
##if number == 2:
##    points = 5
##elif number == 4:
##    points = 14
##elif number == 8:
##    points = 30
##else:
##    points = 0
##    
##print(points)

# key and value pair for dictionary

##book_dict = {2 :f"5", 4 : f"15", 8 : f"30"}

##print(f"Number of points {book_dict.get(number, 0)}")

match number:
    case 2:
        points = 5
    case 4:
        points = 15
    case 8:
        points = 30
    case _:
        points = 0
print(f"Number of points {points}")
