# Function

'''
def function_name:
    code

function_name()
'''

def greet():
    print('hello world')


greet()


# Function with Arguments

def greet(name):
    print(f'hi {name}')

greet('Amir')


def custom_sum(a,b):
    return a + b


resault = custom_sum(5,5)
print(resault)


# Default Arguments


def greet(name = 'User'):
    return f'hi {name}'


print(greet())


# Keyword Arguments

def user_info(name = 'Unkown', age = 18):
    return f'name: {name} and age: {age}'

user_info_1 = user_info(age = 20, name='Amir')

print(user_info_1)


# Args
# برای پارامترهای موقعیتی زیاد

def sum_all(*args):
    return sum(args)


print(sum_all(1,2,3,4,6))



def max_all(*args):
    return max(args)

print(max_all(20,90,91,91.1))

# kwargs
# برای پارامترهای کلیدی زیاد

def user_info(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')

user_info_2 = user_info(name ='Aram', age = 23, city= 'Tehran')
print(user_info_2)

# Recursive function

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(7):
    print(fibonacci(i), end=" ")


# lambda function

square = lambda x: x*x

print(square(4))


# Nested function

def outer(n):
    print(n)
    def inner():
        print('hello')
    inner()

outer('Amir')






def greet():
    return('hello world')

def call_func(func):
    print(func())


call_func(greet)


# Map and Filter

numbers = [1,2,3,4,5,6,8]

square = list(map(lambda x: x**2, numbers))

print(square)


even = list(filter(lambda x: x%2 == 0 , numbers))

print(even)

t = (1,2,3)

t = tuple(map(lambda x: x*x, t))
print(t)

