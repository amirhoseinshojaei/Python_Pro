'''
Data Types:
1- int
2- float
3- complex
4- str
5- list
6- tuple
7- dict
8- set
9- bool
10- None Type
'''


# Numbers in Python

x = 2
y = 3.14
z = 2+3j
print(type(x), x)
print(type(y), y)
print(type(z), z)

print(z.real, z.imag)

a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)

# Strings

s = 'Python Programming'
print(s.upper())
print(s.lower())
print(s.split())

print(s[0])
print(s[1])
print(s[2])
print(s[-3])

# Lists

my_list = [1, 2, 3, 'Python']

my_list.append('R')
my_list.remove('Python')
my_list[0] = 10
print(my_list)

# Tuples
my_tuples = (1,2,3,4)

# my_tuple[0] =10 this is error because tuples are Immutable

# Sets

my_set = {1,2,3,45,3,45}
print(my_set)

my_set.add(5)
my_set.remove(3)
print(my_set)

# Dictionaries
person = {
    'name':'Amir',
    'age':23,
    'city':'Berlin',
    'job':'Software Engineer'
}

person['job'] = 'Data Analyst & Data Scientist'
print(person)

# Join Method

seprator = '-'
words = ['python','Programming','Data Scientist']
result = seprator.join(words)

print(result)

result2 = ' '.join(words)
print(result2)

mixed_list = ['Amir', 'age', 'is', 23]
output = ' '.join(map(str, mixed_list))
print(output)