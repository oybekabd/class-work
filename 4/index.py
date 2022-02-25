# age = int(input('Сколько лет ?'))
# age = '23'
# if (age)>(18):
#   print('Welcome') 

# year = int(input('Введите год - '))
# if(year%400==0):
#     print('Высокосный год')
# elif(year%4==0 and year%100!=0):    
#     print('Высокосный')
# else:
#     print('Не высокосный')    

# a = int(input('Введите число'))
# if(a%2==0):
#     print('Четное')
# else:
#     print('нечетное')

a = int(input('Введите число - '))
if(a>=21):
    g = a-21
    j = g/4 + 2
elif(a<21):
    h = a/10.5
    j = h    
elif(a<0):
    print('Ошибка')
print(j)  
 

