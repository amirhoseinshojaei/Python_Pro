# while

'''
while condition:
    code

'''


i =1

while i<= 5:
    print(i)
    i+=1



#Infinity loop

while True:
    print 


i = 1

while i<=10:
    if i == 5:
        break
    print(i)
    i+=1


i = 0

while i<5:
    i+=1
    if i == 3:
        continue
        print(i)


i = 1

while i<3:
    print(i)
    i+=1
else:
    print('End of the loop')


#Nested while

i = 1

while i<=3:
    j = 1
    while j<=2:
        print(f'i={i}, j={j}')
        j +=1
    i += 1

password = ""

while password != '1234':
    password = input('Enter your password:')
else:
    print(password)

while True:
    password = input('Enter Your password:')


    if len(password) <= 4:
        print('Password must 5 or greather than character')
        continue

    
    if password != '':
        print(password)
        break



