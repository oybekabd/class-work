# Loop - цикл

# ! 2 вида цикла:
# ! while
# ! for

# for i in range(10):
#     print(i, end='\t') 



# range(stop) -> [0; stop)
# range(start, stop) -> [start; stop)
# range(start, stop, step)

# for i in range(200, 100, -2):
#     print(i,)

# for i in range(1 , 11):
#     print('9 * '+str(i) + '=' + str(i*9) ,  ' ')

# for i in range(1, 11):
#     print(f'9 x {i} = {9 * i}')

# def print_exp_table(num, from_num, up_to):
#     for i in range (from_num, up_to + 1):
#         print(f'{num} ** {i} = {num **i}')
# print_exp_table(21,7,13)

for i in range(5, 11):
           print(i/10  )       

# ! один проход цикла - итерация
# for letter in 'OYBEK ABDUQODIROV':
#     if letter == ' ':
#         continue
#     else:
#         print(letter, end='*')

# for letter in 'OYBEK ABDUQODIROV':
#     if letter == ' ':
#         break
#     else:
#         print(letter, end='*')

# print('Oybek'.upper())
# print('OYBEK'.lower())
# print('OYBEK'. isupper())
# print('oybek'.islower())
# print('1'.isdigit())


# new_str = ''
# for letter in 'Elbek khakimbekov is a teacher':
#      new_str = new_str + letter.swapcase()
# print(new_str)    



