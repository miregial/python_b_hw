#!/usr/bin/env python
# coding: utf-8

# In[14]:


#количество  вызовов
count = 0
def fib(n):
    global count #видна глобальна вне этой функции и сохраняет значения между вызовами функции . не  юзают сейчас
    count += 1
    return n if n < 2 else fib(n - 1) + fib(n - 2)


n = int(input("n -> "))
print(f"fib({n}) = {fib(n)}")
print(f"Количество вызовов = {count}")


# In[15]:


#точное считание чисел фиб быстро и для больших чисел с помощью перемножения матриц
def fib(n):
    return _fib(n)[0]


def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


n = 1000 #число
print(f"fib({n}) = {fib(n)}")


# In[22]:


import math
math.cos(math.radians(2))


# In[ ]:


#для дз нужно создать пепременную с суммой и поделить на количество будет ответом


# In[33]:


#преобразовать радианты в градусы так
a= math.pi
2*180/a
#2- радианы с контрольной 2


# In[48]:


#просто делать соответствия
def f(n): 
    return "yes" if n>=7 else "no"
n= int(input())
print(f(n))


# In[ ]:


from math import factorial as fact

print('числа, равные сумме факториалов своих цифр')
k = []
for i in range(0, 10000000000000):
    s = sum([fact(int(x)) for x in str(i)]) 
    if s == i:
        print(i) 
        k.append(i)

if len(k) == 0: print('Таких чисел нет')


# In[ ]:




