# یک ساختار داده ایی در پایتون هست که می تواند مقادیر مختلفی را در یک متغیر ذخیره کند

'''
features :
    1- mutable
    2- ordered
    3- Allowe Duplicates
    4- Support all Data types
'''


my_list = []

mixed_list = ['Amir','Ali',3]

# Indexing

fruits = ['apple','banana','cherry']

print(fruits[0])
print(fruits[1])
print(fruits[2])

# Slicing

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print(numbers[0:5])
print(numbers[0:2])
print(numbers[:6])
print(numbers[2:])
print(numbers[::-1]) # reverse


# Change Value

print(fruits)
fruits[0] = 'Orange'
print(fruits)

# Methods

fruits.append('Banana')
print(fruits)

fruits.insert(1, 'Milk')
print(fruits)

fruits.remove('Milk')
print(fruits)

last = fruits.pop()
print(last)

first = fruits.pop(0)
print(first)


# Search in the list

print(10 in numbers)

print(numbers.index(30))

print(fruits.index('cherry'))

print(numbers.count(10))

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 30, 60]

print(numbers.count(60))


numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)


numbers.sort(reverse=True)
print(numbers)


# Copy the list

copy_numbers = numbers.copy()
print(copy_numbers)

print(copy_numbers is numbers)

copy_numbers2 = numbers
print(copy_numbers2)

print(copy_numbers2 is numbers)

numbers3 = numbers[:]
print(numbers3 is numbers)

numbers.clear()
print(numbers)
print(copy_numbers2)


for fruit in fruits:
    print(fruit)


i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

# List Comprehension

numbers = [x ** 2 for x in range(10)]
print(numbers)


# Merged list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print(merged)

# Repetition

numbers = [1, 2, 3] * 3
print(numbers)

# Filter

numbers = [10, 15, 14, 98.8, 50]

filtered = [ x for x in numbers if x > 20]
print(filtered)

# Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]

print(matrix[0][2])





