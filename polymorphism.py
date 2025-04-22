# Polymorphism

class Cat:
    def sound(self):
        print('Meow')



class Dog:
    def sound(self):
        print('Hop Hop')



animals = [Cat(), Dog()]


for animal in animals:
    print (animal.sound())



# Polymorphism in inheritance

class Animal:
    def speak(self):
        print('Animal Sound')



class Bird(Animal):
    def speak(self):
        print('Che Che')




b = Bird()

print(b.speak())

def animal_speak(animal:Animal):
    animal.speak()



animal_speak(Bird())

animal_speak(Animal())

# Overloading

class Math:
    def add(self, *args):
        return sum(args)
    


m = Math()

print(m.add(2,3,4))

