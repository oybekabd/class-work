


a = int(input('количество квартир - '))
b = int(input('количество этажей - '))
c = int(input('номер этажа друга- '))
if (c<1 or a<1 or b<1): 
       print('error') 
else:            
   d = a//b
   f = c//d
   g = d%c
   
if(c<d):
     f=f+1
if(g>0):
     f=f+1
print(f)        