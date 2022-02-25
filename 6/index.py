# a = int(input('часы'))
# b = int(input('минуты'))
# c = int(input('разница'))

# if(a+c+24):
#     d = (a+c)%24
# else:
#     d = a+c
# if(a+c<0):
#     d = (a+c)%-24



















# v1 = float(input('Введите скорость фвтомобиля из Ташкента: '))
# v2 = float(input('ведите скорость грузовика из Бухары: '))
# t = float(input('Введите часы через сколько они встретилсь: ')) 
# print ((v1 + v2) * t, 'km')


# def (define) 

# def  название_функции(параметр1, параметр2, ...):
#     тело функции
#     в большинстве функций у вас будет присуствовать return

# Название функции должно быть ГЛАГОЛОМ или должно содержать ГЛАГОЛ

# def find_distance(): snake_case (змеинная_запись)
# def findDistance(): camelCase (верблюжья запись)

# def find_distance(v1, v2, t):
#     return (v1 + v2) * t 


# v1  = float(input('Введите скорость 1: '))
# v2 = float(input('Введите скорость 2: '))
# t = float(input('Введи время: '))

# print(find_distance(v1, v2, t))


# print()
# input()
# int()
# str()
# float()
# bool()
# len()
# round()


# + -
#  if in is not


# def Name_my(name):
#     return 'Hello,' + name
# имя = input ('Введите имя: ')
# print(Name_my(имя)) 


# def sum(a, b):
#     return a + b 
 
#  print(sum(2,3))


# def  
#     if a > 0 and b > 0: return a + b 
#     else: return 'Your number are not positive'

    # if a < 0 or b < 0: return 'Your numbers are NOT positive'
    # else: return  a + b  


# def absolute_value(num1):
#      if num1 < 0:
#          print(num1*(-1)) 
#      else:
#          print(num1)

# num = int(input('Введите число'))
# absolute_value(num)      


def absolute_value(num1, num2):
    a = 1
    while(a<=num2):
        num1 = num1*num1
        a+=1
    print(num1)                                        

num = int(input('введите число: '))
num2 = int(input('Введите число: '))
absolute_value(num)


