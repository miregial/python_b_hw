#!/usr/bin/env python
# coding: utf-8

# In[67]:


A = {1,5,6}
B = {1,2,4,5}
C = A.intersection(B)
def f(x,y):
    if (x in C or y in C)==True:
        print('True')
    else:
        print('False')
    
f(1,5)


# In[58]:


A = {1,5,6}
B = {1,2,4,5}
C = A.intersection(B)
print(5 in C)


# In[41]:


primes = {2, 3, 5, 7, 11}
for num in primes:
    print(num)


# In[49]:


A = {1,5,6}
B = {1,2,4,5}
A.intersection(B)


# In[71]:


from math import*
x = float(input("x="))
y = float(input("y="))
r = float(input("r="))
h = sqrt(x**2 + y**2)
print("Расстояние до точки от начала координат равно %.2f" % h)
if h > r:
    print("точка находится за пределами круга")
else:
    print("точка принадлежит кругу")


# In[ ]:




