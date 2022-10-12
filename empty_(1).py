#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Гипотеза простых чисел Гольдбаха утверждает, 
#что любое четное число можно представить в виде суммы двух 
#простых чисел. Давайте напишем программу проверяющую эту гипотезу дляпредварительно заданого числа
def is_prime(num):
    i = 1
    while i < num:
        if num % i == 0:
            return False 
            break
        i += 1
        
    if i == num:
        return True

print("Введите чётное число:")
num = 1
while num%2  != 0:
    num = int(input())

simple_1 = num/2
simple_2 = num/2

while simple_1 < 1 and simple_2 < num:
    is_simple1 = true
    is_simple2 = true
    # что делать дальше догадайтесь сами
    
a=num/num
b=num-a
c=b/b
d=b-c
if a is  is_prime(num):
    print (a,'+',b)
else:
    print(b, ". далее:")
    print(a+ c,'+',d)
if d is not is_prime(num):
        print(d,'далее')
        e = d/d
        f=d-e
        print(a+c+e,'+',f)
else:
        print (a,'+',b)


# In[2]:


#Основная теорема арифметики гласит, что любое составное целое число
#представлятся в виде произведения простых сомножителей, причем единственным образом. 
#Например 50 = 255. Напишите программу, которая для данного числа печатает его разложение на простые сомножители.
def is_primee(num):
    i = 1
    while i < num:
        if num % i == 0:
            return False 
            break
        i += 1
        
    if i == num:
        return True

g=num/2

num = int(input())
if is_prime(num):
    print(f"Число {num} простое")
    print('1 x',num)
else:
    print(f"Число {num} составное")
if num%2 is 0 :
    print(g, '*', 2)
    if g is not is_prime(num):
        h=g//2
        print(h, '*', 2,'*',2)


# In[ ]:





# In[ ]:




