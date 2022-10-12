from sympy import *
init_printing()
a =int(input())
b = int(input())
c =int(input())
if a<0 or b<0 or c<0 or a>=b+c or c>=a+b or b>=a+c:
    print('Error')
else:
    p = (a+b+c)/2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)
from os import system
system("pause")