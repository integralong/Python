#Week 8 Lecture 1

#-----functions definitions-----


#this function uses default parameters
#default parameters have values assigned in its defintion
def prindate(month, day, year = 2023, style =1):
    if style == 1:
        print(f'{month} / {day} / {year}')
    elif style == 2:
        print(f'{day} / {month} / {year}')
    elif style == 3:
        print(f'{year} / {month} / {day}')
    else:
        print('Invalid format')

#this function illustrates keyword arguments
def studentinfo(name, age, gender, grade):
    print(f'Name:{name}\nAge:{age}\nGender:{gender}\nGrade:{grade}')

def main():
    #test function with default parameters
    prindate(10, 11)#using both default parameters
    prindate(11, 1, 2024)#using one default parameter
    prindate(12, 25, 2025, 2)#using no default parameters

    #call studentinfo without keyword arguments
    studentinfo(23, 'A', 'Jane Doe', 'female')#values are placed out of order

    #call studentinfo with keyword arguments
    studentinfo(age = 23, grade = 'A', name = 'Jane Doe', gender = 'female')

    number = int(input('Enter a number:'))
    number2 = int(input('Enter another number:'))
    #lambda function - small anonymous function
    val = lambda n: n + 5
    minus = lambda a, b: a - b
    print(val(number))
    print(minus(number, number2))


#refer -> zybook 6.14.1:A recursive function example

#-----no function definitions below this line-----
main()
















