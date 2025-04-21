# Decorators are High Order Function


def outer():
    print('hello from outer')

    def inner():
        print('hello from inner')

    return inner()


f = outer()


def my_decorator(func):
    def wrapper():
        print('Before function')

        func()

        print('After Function')

    return wrapper



@my_decorator
def say_hello():
    print('hello world')


s = say_hello()


# Decorator with Argument

def my_decorator_2(func):
    def wrapper(*args, **kwargs):
        print('Start')
        resault = func(*args, **kwargs)
        print('End')
        return resault
    return wrapper



@my_decorator_2
def add(a,b):
    return a + b


print(add(2,2))


print(add.__name__)

print(add.__doc__)


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper

    return decorator



# @wraps
from functools import wraps

def my_decorator_3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Befor Start')
        resault = func(*args, **kwargs) * 3
        return resault
    return wrapper

@my_decorator_3
def my_func(a, b):
    return a , b

print(my_func(2,2))


print(my_decorator.__name__)
print(my_decorator.__doc__)


