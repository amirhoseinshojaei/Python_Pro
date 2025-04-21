x = [1,2,3,4]

it = iter(x)

print(next(it))

print(next(it))


while True:
    try:
        print(next(it))
    
    except StopIteration:
        break



# while True:
#     print(x)


def my_gen():
    yield 1
    yield 2
    yield 3


print(my_gen())

for i in my_gen():
    print(i)