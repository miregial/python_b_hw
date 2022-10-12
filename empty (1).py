#!/usr/bin/env python
# coding: utf-8

# In[6]:


from sympy import *
init_printing()
var ('x')


# чтобы найти точки перегиба  - надо найти две производные , - это максимум  а + минимум(правило зонта)
# 

# In[7]:


f = x**5 + 4*x**4 - 13*x**3 +8
f


# In[9]:


f1 = diff(f,x)
f1


# In[39]:


nrs = nroots(f1, n=2) # численные корни  solve - символьные корни
nrs


# In[25]:


f2 = diff(f1,x)
f2


# In[40]:


f2.subs(x,0) #=0 значение функции в точке


# In[29]:


[f2.subs(x,i) for i in nrs] #вывод списка корней


# In[30]:


[y**2 for y in range(1,11)] #получили список квадратов


# In[33]:


ls = []
for y in range(1,11):
    ls.append(y**1)
ls


# In[38]:


#список занчений вторых производных для контрольной
ls = [y**2 for y in range(1,11)]
ls


# In[49]:


#с помощью цикла приравнивали критические точкти к 0 
for y in nrs:
   if f2.subs(x,y)>0:
       print (f"f2({y}) = {f2.subs(x,y)}") 
       


# In[43]:


[f2.subs(x,y) for y in nrs]


# In[ ]:




