#!/usr/bin/env python
# coding: utf-8

# In[1]:


#факториал с помощью цикла
from sympy import *
init_printing()
def factorial(n):
    f=1
    for k in range(2,n+1): #начали диапозон с 2х , потому что умножение на 1 ничего не меняет
        f=f*k #можно еще написать как f*=k
    return f
factorial(100)


# In[2]:


#СКОЛЬКО ЦИФР В ЧИСЛЕ
#1. превратил в строку (стр ту инт)
n = factorial(1000) #для факториала 1000
s = str(n)
type(s)
len(s)  #2. длина строки и есть количество цифр 


# In[3]:


#итерационные версии числа Фибонначе a,b = 1,1 
def fib(n):
    a,b = 1,1
    for k in range(n): #старое число будет становиться как б , но  последующее после б это а+б (1,1,2,3,5,8)
        a,b = b, a+b
    return a
fib(4)


# In[8]:


#ТЕПЕРЬ НЕ ОТ 0 А ОТ 1 БУДЕТ ТЕПЕРЬ итерационные версии числа Фибонначе a,b = 1,1  ЭТО 25 ЗАДАЧА ИЗ ПРОЕКТА ЭЙЛЕРА
def fib(n):
    a,b = 1,1
    for k in range(1,n): #старое число будет становиться как б , но  последующее после б это а+б (1,1,2,3,5,8)
        a,b = b, a+b
    return a
def len_fib(size):
    k=1
    len_fib = len(str(fib(k)))
    while len_fib<size:
        k+=1
        len_fib  = len(str(fib(k)))
    return (k, fib(k))
len_fib(3)


# In[6]:


#решить дома 34 задачу из проекта эйлера  miregial 02022000erary


# In[11]:


def len_fib(size):
    k=1
    len_fib = len(str(fib(k)))
    while len_fib<size:
        k+=1
        len_fib  = len(str(fib(k)))
    return (k, fib(k))
len_fib(1000)


# In[ ]:





# In[ ]:




