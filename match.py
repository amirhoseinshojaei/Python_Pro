# Match


'''
match value:
    case value1:
        code
    case value2:
        code
    case_:
        default

'''



day = 'شنبه'

match day:
    case 'شنبه':
        print('اول هفتس')
    case 'جمعه' | 'پنج شنبه':
        print('تعطیل است')
    case _:
        print('روز کاری')



file_extension = 'jpg'

match file_extension:
    case 'jpg' | 'png' | 'gif':
        print('این یک فایل تصویری است')
    case 'mp4' | 'mkv':
        print('این یک فایل ویدویی است')
    case _:
        print('ناشناس')


# Case Variable

num = 10

match num:
    case 1:
        print(1)
    case 2:
        print(2)

    case other:
        print(other)



data = ['Amir', 23]

match data:
    case ['Aram', age]:
        print(f'years:{age}')
    case other,year:
        print(f'years:{year}')


age = 20

match age:
    case x if x<18:
        print('Teenager', x)

    case x if 18<=x<=30:
        print('Young',x)
    case _:
        print('Adult')



# Use match in class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Aram', 15)

match person:
    case Person(name = 'Aram', age= 25):
        print('Aram is 25 y')
    case Person(name = 'Aram', age = 15):
        print('Aram is 15 y')
    case _:
        print('Unkown')
        

