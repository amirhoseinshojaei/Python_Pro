'''
A variable in Python is a named storage location used to hold data. It acts as a container that stores values,
which can be changed during program execution.
'''


x = 10 # Integer

y = 3.14 # Flot

name = 'Amir' # String

is_valid = True # Boolean

print(type(x))
print(type(y))
print(type(name))
print(type(is_valid))

a,b,c = 10,15,'amir'
print(a)
print(b)
print(c)

x = int(3.14)
y = float(10)
z = str(11)
m = int('35')

print(x, type(x))
print(y, type(y))
print(z, type(z))
print(m, type(m))

# Scope

x = 102 # Global

def my_fun():
    y = 50 # Local
    print(y)


def my_func2():
    global x
    x = 100


my_func2()
print(x)

y = x

print(y)

# Mutable Variables and Immutable Variables

# Mutable = list - dict - set

# Immutable = str - int - float - tuple

'''
exp) y = "hello"
    y[0] = u
    This is wrong  
'''

# Delete Variables

# del x
#
# print(x)

x = None
print(type(x), x)


print(bool(0))
print(bool(1))