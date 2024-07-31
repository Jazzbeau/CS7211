#!/home/jazzbeau/anaconda3/bin/python
from random import randint

my_var1,my_var2,myvar3 = randint(1,100),randint(1,100),randint(1,100)
if my_var1 > my_var2:
	if my_var1 > my_var3:
		print(f'{my_var1} is the largest')
	else:
		print(f'{my_var3} is the largest')
elif my_var2 > my_var3:
	if my_var2 > my_var3:
		print(f'{my_var2} is the largest')
	else:
		print(f'{my_var3} is the largest')
