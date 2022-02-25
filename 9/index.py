# инициализация переменной 
# while условие:
# тело цикла

# ! В цикле while условие когда-то должно стать FALSE
# ? В условие есть переменная, которая должна меняться при каждом проходе цикла 
# * Переменная меняется в теле цикла 
# ! Обычно переменная является счётчиком 

# Пример вывода чисел от 10 до 20 вклюительно 
# i = 10
# while i <= 20:
#     # print(i)
#     print(i, end= ' ')
#     i = i + 1    


# for i in range(10, 21):
#     print(i, end=' ')


# Пример вывода чисел от 200 до 150 включительно, десятками 

# for i in range(200, 149, -10):
#     print(i, end=' ')


# i = 200
# while i >= 150:
#     print(i, end=' ')
#     i = i - 10

# name = 'Hello! I am Oybek. Wassup'

# индексы должны быть целым числомб а иначе будет ошибка
# i = 0
# while i < len(name):
#     print(name[i], end='/')
#     i += 1

# for ltr in name:
#     print(ltr, end='/')

# for i in range(len(name)):
#     print(name[i], end='/')

# Способы создать бесконечный цикл
# 1. Написать условие, которое всегда будет верным


# while 1 > 0:
#     pass


# 2. В условие написать True

# while True:
#     pass

# Как остановить циклб который бесконечный ->Нужно, чтобы консоль была активной и нажать Ctrl + C 


# Как уравлять циклом, который бесконечный?
# Ответ -> с помощью if и break

# i = 0 
# while True:
#     print('Oybek')
#     i = i + 1
#     if i == 3:
#         break


# while True:
#     num = int(input('Enter positive number: '))
#     if num  < 0:
#         break

# int
# float
# bool

# ! Индексируемый объекты 
# str
# list

# Гомогенный список -> потому, что в нём только СТРОКИ
students = ['Umar', 'Abduvali', 'Oybek', 'Iskandar' ]
ages = [16, 16, 16, 13, 14, 15]
countries = ['Uzbekistan', 'Usa', 'Germany', 'Poland', 'Sweden']
country_codes = ['UZ', 'PO', 'UK', 'UA']


F1_drivers = ['Max', 'Lewis', 'Sebastian', 'Daniel', ]
f1_car_nums = ['33', '44', '5', '3']
constructors = ['mercedes', 'redbull', 'astonmartin', 'mclaren']
tires = ['soft', 'medium', 'hard']
tracks = ['silverstone', 'dutch', 'austin']
flags = ['green', 'yellow', 'red']
pitstops = ['1', '2', '3', '4']
places = ['1', '2', '3']
best_world_champions = ['7 - shumacher', '7 - hamilton', '4 - vettel']
machine_functions = ['DRS', 'SLEEPSTREAM', 'VOICE CHAT'] 


