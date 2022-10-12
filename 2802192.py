from sympy import *
init_printing()
a=int(input('vvedite 3x znachnoe chislo'))
if a<100 or a>=1000:
    print ('chislo ne 3x znachnoe')
else:
    b = a%10
    c = a//100
      d = (((a%100)- (a%10))//10)
    print (b,c,d)
from os import system
system("pause")