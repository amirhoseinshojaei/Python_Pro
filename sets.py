# یک نوع داده ایی در پایتون هست که شامل عناصر منحصر به فرد و نامرتب است


'''
Features:
    1- mutable
    2- Unordered
    3- Unique Values
    4- Support for mathematical operations
    such as addition, subtraction, and multiplication
'''

empty_set = set()

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

mixed = {1, 2, 3, 4, 5, 6, 7, 8, 9, 'Python', True, False}

# Automatic remove duplicates

my_set = {1,2,2,4,5,6,7,7,8,9,9}

print(my_set)

# Convert list to set

my_list = [1,2,2,3,3,44,44,]

my_set = set(my_list)

print(my_set)


# Acces to set values

for value in my_set:
    print(value)

# Methods

numbers.add(5)

numbers.update('Python', 'Java')
print(numbers)


numbers.update(['Python', 'Java'])
print(numbers)

numbers.remove('Python')
print(numbers)

numbers.discard('Python')

random = numbers.pop()
print(random)

numbers.clear()
print(numbers)


# unio

A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
B = {1, 2, 3, 4, 30, 6, 7, 80, 9}

print(A | B)

print(A.union(B))

# Intersection

print(A & B)
print(A.intersection(B))

# Difference

print(A - B)
print(A.difference(B))


# Symmetric difference

print(A ^ B)
print(A.symmetric_difference(B))


# Relationship review

print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(B))


# Copy set

copy_numbers = numbers.copy()
print(copy_numbers)

# Frozenset

a = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9})
print(a)
