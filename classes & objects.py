# کلاس مثل نقشه ساختمونه و object همون ساختمونیه که از روش ساخته شده

'''
class Person:
    pass
    



'''

# Build a simple class

class Person:
    pass


# Build a object

p1 = Person()

print(type(p1))


# __init()__ متود سازنده

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Amir', 23)

print(p1.name)
print(p1.age)
        


class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def greet(self):
        print(f'hello {self.name}')


p1 = Person('Amir', 'Tehran')

p1.greet()



class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    def car_info(self):
        print(f'wheels:{self.wheels}, brand: {self.brand}')


car_1 = Car('BMW')
car_2 = Car('Benz')

car_1.car_info()
car_2.car_info()
        
# __str__ method

# برای نمایش شی به شکل زیباتر

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f'Book: {self.title}'


book_1 = Book('Data Analytics')
book_2 = Book('Data engineer')

print(book_1)

print (book_2)


class Plus:
    def __init__(self, number_1, numbers_2):
        self.number_1 = number_1
        self.number_2 = numbers_2

    def add(self):
        return self.number_1 + self.number_2
    
    def __str__(self):
        return f'{self.number_1} , {self.number_2}'
    

plus_1 = Plus(2,2)

print(plus_1, plus_1.add())

        
# Inheritance

class Animal:
    def speak(self):
        print('Animal Sound')


class Dog(Animal):
    def brak(self):
        print('Hop Hop')


d = Dog()

d.brak()

d.speak()


# Polymorphism

class Cat:
    def speak(self):
        print('Meow')


class Dog_2:
    def speak(self):
        print('Hop Hop')


for animal in [Cat(), Dog_2()]:
    animal.speak()



# Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance__ = balance     # Private

    def get_balance(self):
        return self.__balance__
    


acc = BankAccount(10000)

print(acc.get_balance())
        

# @classmethod

class Person:
    count = 0
    def __init__(self):
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    

p1 = Person()
p2 = Person()
print(Person.get_count())


# @staticmethod

class Math:
    @staticmethod
    def add(a, b):
        return a + b
    

print(Math.add(5,3))


# Destructor


class File:
    def __del__(self):
        print('Destructor')



f = File()

del f

# isinstance

print(isinstance(d,Dog))



# hasattr(), gettatr(), setattr(), delattr()

class Person:
    def __init__(self):
        self.name = 'Aram'


p = Person()
        
print(hasattr(p, 'name'))

print(getattr(p, 'name'))

print(p.name)

setattr(p, 'age', 25)
print(p.age)

delattr(p, 'name')

print(hasattr(p, 'name'))


# Property


class circle:
    def __init__(self, radius):
        self.radius = radius


    @property
    def area(self):
        return 3.14 * self.radius ** 2
    


c = circle(3)

print(c.area)


# Operator Overloading

class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x
    
    def __str__(self):
        return self.x
    


p_1 = Point(2)

p_2 = Point(3)

p_3 = p_1 + p_2

print(p_3)
        




