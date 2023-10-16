#Week 5 lecutre 2

#using match case structure in Python

##status = int(input('Enter status code:'))
##
##match status:
##    case 400:
##        msg = "Bad request" #indented
##    case 404:
##        msg = "Not found" 
##    case 418:
##        msg = "I'm a teapot"
##    case 502:
##        msg = "Bad gateway"
##    case 504:
##        msg = "Gateway timeout"
##    case _: #wildcard
##        msg = "Something's wrong with the internet"
##
##print(msg)
##
##
###example 2 : how to match a range (use with caution)
##score = int(input('Enter a score(integer from 0 to 100):'))
###input validation
##while score < 0 or score > 100:
##    score = int(input('Invaild. Enter a score(integer from 0 to 100):'))
##
##match score // 10:
##    case 10 | 9: # | repesent or (for scores 90 to 100)
##        print('Grade is A')
##    case 8:
##        print('Grade is B')
##    case 7:
##        print('Grade is C')
##    case 6:
##        print('Grade is D')
##    case _:
##        print('Grade is F')
        

#count-controlled while loop
i = 1 #initialization
while i <= 5: #condition
    print(f'i is {i}')
    i = i + 1 #update 
print()

#for loop
for j in range(5): #5 is the upper limit (normally exclusive)
    print(f'j is {j}')
print()

for j in range(1,11,2): #1 is the lower limit(incl.); 5 is the upper limit(excl.), step = +2
    print(f'j is {j}')   
print()


#break and continue with loop

for k in range(10):
    if k == 4:
        break #completely interrups the loop
    print(k, end=' ')
print()  


for k in range(10):
    if k == 4:
        continue 
    print(k, end=' ')
print()



#loop else
for n in range(1,11):
    if n == 7:
        break #toggle between continue and break
    print(n, end=' ')
else: #runs as long as the loop completes(most) of its iterations
    print('The loop has ended')

while True:
    #....
    if....:
        break










