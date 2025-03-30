'''
Operators:
1- Arithmetic Operators
2- Comparison Operators
3- Logical Operators
4- Assignment Operators
5- Bitwise Operators
6- Membership Operators
7- Identity Operators
'''

# Arithmetic Operators

print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)
print(5 % 5)
print(5 ** 5)
print(5 // 5)


# Comparison Operators

print(5 == 6)
print(5 != 6)
print(5 <= 6)
print(5 > 6)
print(5 >= 5)
print(5 < 6)

# Logical Operators

print((5==5) and (6 > 5)) # 2 statement are True

print((6 < 5) and (5 != 6))

print((6 < 5) or (5 != 6))

print(not (6 < 5))

# Assigment Operators

x = 3
x += 3
x-=3
x *= 4
x /= 3
x %= 3
x //=3
print(x)

# Bitwise Operators

print(5 & 3)
print(5 & 0)
print(5 | 3)
print(5 | 1)
print(5 | 0)
print(5 | 6)
print(5 ^ 3)
print(5 << 1)
print(5 >> 1)

# Membership Operators

a = 'apple'
print('a' in a)
print('b' in a)
print('b' not in a)

# Identity Operators

x = [1,2,3]
y = x
z = [1,2,3]
l = x.copy()

print(x is y)
print(x is z)
print(x is l)

print(x is not z)