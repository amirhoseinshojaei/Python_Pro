# Conditions

'''
if condition:
    run code

'''

age = 18

if age >= 18:
    print('Positive')


age = 16

if age >= 18:
    print('Positive')
else:
    print('Negative')



score = 75

if score >= 90:
    print('Super')

elif score >= 75:
    print('Gut')

elif score >= 50:
    print('Nicht gut')

else:
    print('Awful')


age = 25
income = 3000

if age > 18 and income >= 4000:
    print('Receiver')
elif age >= 20 or income >= 2500:
    print('Yep')

else:
    print('Nothing')


age = 20
is_student = True

if age >= 18:
    if is_student:
        print('شما دانشجوی بالای 18 سال هستید')
    else:
        print('شما بالای 18 سال هستید اما دانشجو نیستید')
    
else:
    print('شما زیر 18 سال هستید')


# Ternary Operators
age = 20
message = 'Big' if age>=18 else 'Small'

print(message)


if age >= 25:
    pass






