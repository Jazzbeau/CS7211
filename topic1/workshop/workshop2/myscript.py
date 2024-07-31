#/home/jazzbeau/anaconda3/bin/python
from random import randint

myvar1,myvar2,myvar3 = randint(1,100),randint(1,100),randint(1,100)

if myvar1 > myvar2:
    print(f'{myvar1} is the largest') if myvar1 > myvar3 else print(f'{myvar3} is the largest')
elif myvar2 > myvar3:
    print(f'{myvar2} is the largest') if myvar2 > myvar3 else print(f'{myvar3} is the largest')
