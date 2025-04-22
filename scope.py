# Scope



'''
Some of Scope: Local. Encsoling, Global, Built-In
'''

# Local Scope

def my_func():
    x = 10
    print(x)


my_func()

# print(x)


# Global Scope

x = 5

def show():
    print(x)


show()

print(x)


# Global Keyword

def modify():
    global y
    y = 20
    print(20)


modify()

print(y)


# Nonlocal Keyword

def outer():
    x = 'outer'

    def inner():
        nonlocal x
        x = 'modify'
    inner()

    print(x)



outer()


# Built-in like sum(), min(), max(), range(), len

