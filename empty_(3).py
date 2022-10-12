#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Примеры рекурсивных функций и рекурсивных программ/ Вычисление факториала:
def fact(n):
    return 1 if n == 0 else n*fact(n - 1)


n = int(input("n -> "))
print(f"{n}! = {fact(n)}")


# In[ ]:


#Нахождение чисел Фибоначчи:
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


n = int(input("n -> "))
print(f"fib({n}) = {fib(n)}")


# In[ ]:


#количество входных данных сколь угодно велико. 
#нахождение суммы элементов последовательности.бесконечный цикл while True,
#выход только в случае исключения (Exception) — завершения обрабатываемой последовательности
#пустая строка - ошибка и выдаст конец
s = 0
try:
    while True:
        s += int(input("x -> "))
except(EOFError):
    print(f"\n      s = {s}")


# In[ ]:


s = 0
try:
    while True:
        s += int(input("x -> "))
except(EOFError, ValueError):
    print(f"\n      s = {s}")


# In[ ]:





# In[ ]:




