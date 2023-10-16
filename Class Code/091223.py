#Week 4 Leucture

#recap of selection
score = float(input('Enter a score:'))
if score >= 80:
    print('Yay')
    print('You advance!')
else:
    print('Oh no!')
    print('Try again')

#same exaple with conditional(ternary)form
#print(true outcome if condition else false outcome)

print('Yay! You advance!'if score >= 80 else 'Oh no! Try again!')

#same example with walrus operator
if score := float(input('Enter a score:')) >= 80:
    print('Yay!')
    print('You advance!')
else:
    print('Oh no!')
    print('Try again!')

#same example with walrus operator and ternary form
print('Yay! You advance!'if (score := float(input('Enter a score:')) >= 80)else 'Oh no! Try agian!')


#multiple selection
score = float(input('Entr a score:'))

#nested if else structure
if score >= 90:
    grade = 'A'
else:
    if score >= 80:
        grade = 'B'
    else:
        if score >= 50:
            grade = 'D'
        else: #trailinng else
            grade = 'F'
print(f'The grade is {grade}')

#if elif structure

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 65:
    grade = 'C'
elif score >= 50:
    grade = 'D'
else:#trailing else
    grade = 'F'
print(f'The grade is {grade}')

#series of if statements
# (upper limits defined)
#interpreter has to check every condition
if score >= 90 and score < 107:
    grade = 'A'
if score >= 80 and score < 90:
    grade = 'B'
if score >= 65 and score < 80:
    grade = 'C'
if score >= 50 and score < 65:
    grade = 'D'
if score >= 0 and score < 50 :#trailing else
    grade = 'F'
print(f'The grade is {grade}')


#same as previous example, but uses relational operators only
#flip the first set of relational operators
if score in range(90, 107)
    grade = 'A'
if score in range(80, 90)
    grade = 'B'
if score in range(65, 80)
    grade = 'C'
if score in range(50, 65)
    grade = 'D'
if score in range(0, 50)
    grade = 'F'
print(f'The grade is {grade}')