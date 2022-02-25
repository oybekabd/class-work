# 35
# a = int(input('Введите число'))
# if(a%2==0): 
#     print('Четное')
# else:
#     print('нечетное')

# 36
# a = int(input('Введите число'))
# if(a>=21):
#     g = a-21
#     j = g/4 + 2
# elif(a<21):
#     h = a/10.5
#     j = h
# elif(a<0):
#     print('Ошибка')
# print(j)

# 37
# letter = input('Введите букву: ')

# if letter == 'a':
#    print('Это гласная буква')
# elif letter == 'e':
#     print('Это гласная буква')
# elif letter == 'i':
#     print('Это гласная буква')
# elif letter == 'o':
#     print('Это гласная буква') 
# elif letter == 'u':
#     print('Это гласная буква')
# elif letter == 'y':
#     print('Буква может быть так гласной, так и согласная')   
# else:
#     print('Это согласная буква') 

# 38
# sides = int(input('Введите количество сторон фигуры: '))

# if sides < 3:
#     print('Не существует такой геометрический фигуры!')
# elif sides == 3:
#     print('Это треугольник')
# elif sides == 4:
#     print('Это четырехугольник')
# elif sides == 5:
#     print('Это пятиугольник')
# elif sides == 6:
#     print('Это шестиугольник')
# elif sides == 7:
#     print('Это семиугольник')
# elif sides == 8:
#     print('Это восьмиугольник')  
# elif sides == 9:
#     print('Это девятиугольник') 
# elif sides == 10:
#     print('Десятиугольник') 
# else:
#     print('Фигура')

# 39
# month =  str(input('Введите месяц'))
# january = 'january'
# february='february'
# march = 'march'
# april = 'april'
# may = 'may'
# june = 'june'
# july = 'july'
# august = 'august'
# september = 'september'
# october = 'october'
# november = 'november'
# december = 'december'
# if month==january:
#     print('31')
# elif month==february:    
#     print('28 or 29')
# elif month==march:
#     print('31')
# elif month==april:
#     print('30')
# elif month==may:
#     print('31')
# elif month==june:
#     print('30')
# elif month==july:
#     print('31')
# elif month==august:
#     print('31')
# elif month==september:
#     print('30')
# elif month==october:
#     print('31')
# elif month==november:
#     print('30')
# elif month==december:
#     print('31')
# else:
#     print('ERROR')

# 40
# something=int(input('Введите громкость:'))
# lawnmower=106
# hammer=130
# alarm=70
# room=40
# if something==106:
#     print('lawnmower')
# elif 106<something<130:
#     print('voice is between lawnmower and hammer')
# elif something==130:
#     print('hammer')
# elif 70<something<106:
#     print('voice is between alarm and alarm ')
# elif something==70:
#     print('alarm')
# elif 40<something<70:
#     print('voice is between room and alarm')
# elif something==40:
#     print('room')
# else:
#     print('UKNOWN VOICE!')


# 41
# a = int(input('Введите сторону треугольника: '))
# b = int(input('Введите сторону треугольника: '))
# c = int(input('Введите сторону треугольника: '))
# if ((a+b>c) and a+c>b and b+c>a):
#     if(a==b==c):
#         print('Равносторонний')
#     elif(a==b or b==c or c==a):
#         print('Равнобедренный')
#     elif(a!=b or b!=c or c!=a):
#         print('Разносторонний'):
# else:
#     print('Error')

# 44
# banknote =int(input('Enter baknote nominal:'))
# jorj_washington = 1
# Thomas_jefferson = 2
# Abraham_lincoln = 5
# Alexander_hamilton = 10
# Andrew_jackson = 20
# Ullis_grant = 50
# Benjamin_franclin = 100

# if banknote == 1:
#     print('ДЖордж Вашингтон')
# elif banknote == 2:
#     print('Томас Джеферсон')
# elif banknote == 5:
#     print('Авраам Линкольн')
# elif banknote == 10:
#     print('Александер Хамильтон')
# elif banknote == 20:
#     print('Эндрю Джексон')
# elif banknote == 50: 
#     print('Уллис Грант')
# elif banknote == 100:
#     print('Бенджамин Франклин')
# else:
#     print('Такой банкноты не существует!')
    
    # 45
# day = int(input('Введите день:'))
# month = input('Введите месяц:') 
# January='January'
# July='July'
# December = 'December'

# if day ==1 and moth == January:
#     print('New year')
# elif day ==1 and moth == July:
#     print('Canada day')
# elif day ==25 and moth == December:
#     print('Christmas')
# else:
#     print('Error')

# 46
# number = int(input('Введите цифру:'))
# letter = input('Введите букву:')
# a='a'
# b='b'
# c='c'
# d='d'
# e='e'

# if letter == 'a' and number % 2==1:
#     print('Черный')
# elif letter =='a' and number % 2==0:
#     print('Белый')
# elif letter =='b' and number % 2==0:
#     print('Черный')
# elif letter =='b' and number % 2==0:
#     print('Белый')
# elif letter =='c' and number % 2==0:
#     print('Черный')
# elif letter =='c' and number % 2==0:     
#     print('Белый')
# elif letter =='d' and number % 2==0:    
#     print('Черный')
# elif letter =='d' and number % 2==0:
#     print('Белый')
# elif letter =='e' and number % 2==0:        
#     print('Черный')
# elif letter =='е' and number % 2==0:
#     print('Белый')
# elif letter =='f' and number % 2==0:
#     print('Черный')
# elif letter =='f' and number % 2==0:
#     print('Белый')
# elif letter =='g' and number % 2==0:
#     print('Черный')
# elif letter =='g' and number % 2==0:                    
#     print('Белый')
# elif letter =='h' and number % 2==0:
#     print('Черный')
# elif letter =='h' and number % 2==0:
#     print('Белый')

#49
# year = int(input('Enter your year:'))
# a = year%12
# if a ==0:
#     print('Monkey')
# elif a ==1:
#     print('Hen')
# elif a ==2:
#     print('Dog')
# elif a ==3:
#     print('Pig') 
# elif a ==4:
#     print('Mouse')
# elif a ==5:
#     print('Cow')
# elif a ==6:
#     print('Tiger')
# elif a ==7:
#     print('Rabbit')
# elif a ==8:
#     print('Dragon')
# elif a ==9:                                   
#     print('Snake')
# elif a ==10:
#     print('Horse')
# elif a ==11:
#     print('Goat')

# else:
#     print('Error')  

# 48
# month =input('назовите месяц:')
# day =input('назовите день:')

# if month == 'march' and 20<=day<=31 or month == 'april' and 1<=day<=30 or month == 'may' and 1<=day<=31 or month == 'june' and 1<=day<21:
#     print('spring')
# if month == 'june' and 21<=day<=31 or month == 'july' and 1<=day<=30 or month == 'august' and 1<=day<=31 or month == 'september' and 1<=day<22:
#     print('summer')
# if month == 'september' and 22<=day<=31 or month == 'october' and 1<=day<=30 or month == 'november' and 1<=day<=31 or month == 'december' and 1<=day<21:
#     print('autumn')
# if month == 'december' and 21<=day<=31 or month == 'january' and 1<=day<=30 or month == 'february' and 1<=day<=31 or month == 'march' and 1<=day<20: 
#     print('winter')


# 52
# band =input('Введите оценку:')
# number=input('Введите знак:')
# if band == ('A') and number==('+'):
#     print(4.0)
# elif band == ('A') and number==(''):
#     print(4.0)    
# elif band == ('A') and number==('-'):    
#     print(3.7)
# elif band == ('B') and number==('+'):    
#     print(3.3)
# elif band == ('B') and number==(''):
#     print(3.0) 
# elif band == ('B') and number==('-'):
#     print(2.7) 
# elif band == ('C') and number==('+'): 
#     print(2.3) 
# elif band == ('C') and number==(''):                   
#     print(2.0)
# elif band == ('C') and number==('-'): 
#     print(1.7)
# elif band == ('D') and number==('+'):     
#     print(1.3)
# elif band == ('D') and number==(''): 
#     print(1.0)     
# elif band == ('D') and number==('-'):  
#     print(0) 
# else:
#     print('Error!')
