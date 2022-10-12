#!/usr/bin/env python
# coding: utf-8

# In[7]:


from math import gcd
class Frac:

    # n - numerator (числитель)
    # d - denominator (знаменатель)
    def __init__(self, n, d):
        if(d == 0):
            raise ZeroDivisionError
        t = gcd(n, d)
        self.n = n // t
        self.d = d // t

    # разность между «самим» объектом (self) и каким-то иным (other)
    def __sub__(self, other):
        return Frac(self.n * other.d - other.n * self.d, self.d * other.d)
    
    # сумма между «самим» объектом (self) и каким-то иным (other)
    def __add__(self, other):#x.__add__(y)
        return Frac((self.n * other.d).__add__(other.n * self.d), self.d * other.d)
    
    # умножение между «самим» объектом (self) и каким-то иным (other)
    def __mul__(self, other): #- умножение (x * y)
        return Frac(self.n * other.n , self.d * other.d)

    # представление объекта в виде строки
    def __repr__(self):
        return f"{self.n}/{self.d}"

a = Frac(2,3)
b = Frac(3,6)
print(f"{a} - {b} = {(a)-(b)}")
print(f"{a} + {b} = {(a).__add__(b)}")
print(f"{a} х {b} = {(a)*(b)}")
#c = Frac(1,0)


# In[ ]:




