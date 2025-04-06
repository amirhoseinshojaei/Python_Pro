# یک نوع داده ایی در پایتون مثل لیست هست که چندین مقدار را در خود ذخیره میکند

'''
features:
    1- immutable
    2- ordered
    3- Allowed Duplicates
    4- Faster than lists
'''


empty_tuple = ()

numbers = (1, 2, 3)

mixed = (1, 2, 'python', True)

single_element = (1,)

print(type(single_element))

# Convert List to Tuple

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)

# Indexing

fruits = ('apple', 'banana', 'cherry')
print(fruits[0])
print(fruits[2])
print(fruits[-3])


# Slicing

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90)

print(numbers[1:])
print(numbers[2:])
print(numbers[:2])
print(numbers[3:])
print(numbers[::-1])

# Change tuple Values

list_fruits = list(fruits)

list_fruits[2] = 'banana'

print(list_fruits)

fruits = tuple(list_fruits)

print(fruits)

# Methods


print(numbers.count(0))

print(numbers.index(10))

numbers = (10, 10, 20, 0)

print(numbers.count(10))

# Tuple Concatenation

tuple1= (1,2,3)
tuple2=(7,6,5)
merged = tuple1 + tuple2
print(merged)


# Tuple Repetition

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90) * 3
print(numbers)

# Membership Operators in tuples

print(20 in numbers)

print(20 not in numbers)

# Covert to string
words = ('hello', 'world')
sentence = " ".join(words)
print(sentence)

# Search in the tuple

for fruit in fruits:
    print(fruit)



i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1

# Nested tuples

nested_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)

print(nested_tuple[2][0])

# Unpacking

coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)

# Packing
tuple1 = ()
tuple1 = 10, 20, 30
print(tuple1)


# Unpacking2

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90)

a, b, *c = numbers
print(a, b, c)

