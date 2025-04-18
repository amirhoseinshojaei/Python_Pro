# For loop

'''
for x in DataType(list,tuple,.....):
    code

'''

# Loop in lists

names = ['Amir','Alex','Ali']

for i in names:
    print(i)


# Range

for i in range(5):
    print(i)


# Range(Start, Stop, Step)

for i in range(2,12,2):
    print(i)


# Loop in string

text = 'hello User'

for s in text:
    print(s)


# Loop in Dict

user = {
    'name': 'Amir',
    'age': 23,
    'city': 'Tehran'
}

for i in user:
    print(i)


for key in user.keys():
    print(key)


for value in user.values():
    print(f'values:{value}')


for k,v in user.items():
    print(f'key:{k}:values:{v}')


users = {
    'user_1':{
        'name': 'amir',
        'income': 23000
    },
    'user_2':{
        'name': 'aram',
        'income': 20000
    }
}


for i in users:
    print(i)



for k in users.keys():
    print(k)


for v in users.values():
    print(v)


for k,v in users['user_1'].items():
    print(f'{k}:{v}')


# enumerate

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)


for index, k in enumerate(user):
    print(index, k)

# Zip


names = ['Amir', 'Aram', 'Mohsen']
ages = [23, 15, 18]

for n,a in zip(names, ages):
    print(f'{n}:{a}')


# break, continue


for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(10):
    if i == 5:
        continue
    print(i)


# Nested loop

for i in range(10):
    for j in range(8):
        print(f'i ={i}, j = {j} ')
else:
    print('End')
