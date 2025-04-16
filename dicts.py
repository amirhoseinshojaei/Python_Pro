# Dictionaries


'''
Feautured:
1- Unique keys
2- ordered
3- mutable
4- Fast Access

'''

# Build a dict

my_dict = dict()

my_dict_2 = {}

person = {
    'name':'Aram',
    'age': 23,
    'city':'Tehran'
}


person = dict(name = 'Amir', age = 23, city = 'Tehran')


print(person['name'])

print(person['age'])


print(person.get('name'))

print(person.get('country', 'Not Found'))


person['age'] = 25

person['city'] = 'Berlin'

print(person)


del person['age']

person.pop('city')


person.popitem()

person = dict(name = 'Amir', age= 23, city= 'Tehran')

for k in person.keys():
    print(k)


for v in person.values():
    print(v)


for k,v in person.items():
    print('{}:{}'.format(k,v))


print('name' in person)



copy_person = person.copy()

copy_person_2 = dict(person)


print(person is copy_person)

print(person is copy_person_2)



person.update(languages = 'Deutsch', Hobby = 'Go to the Gym')

print(person)

extra_info = {
    'number': '0910....'
}

person.update(extra_info)

print(person)


# Nested Dict

students = {
    'student_1':{'name':'Amir', 'age': 23},
    'student_2':{'name':'Aram', 'age': 15}
}

print(students['student_1']['name'])


# Default collections

from collections import defaultdict

my_dict = defaultdict(int)
print(my_dict)


my_dict['x'] = 1

print(my_dict)
my_dict['y'] = 'a'

print(my_dict)