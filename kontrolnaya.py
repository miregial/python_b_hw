#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sympy import *
init_printing()
var('x')
f = Integral(((((4*x) + 7)**2)*((((3*x)-11))**3)),x)
print(f)
f.doit()
plot(f.doit())


# Задание 1 Постройте график той первообразной функции (4x+5)^2(5x-13)^2, которая в точке x0=-4 принимает значение y0=13850

# In[9]:


a = integrate(f,x)
c = a - a.subs(x,-2)+19992
c.subs(x,-2)
plot(c, (x, -2, 1))


# Задание 2. Найдите площадь треугольника, построенного на векторах 

# In[42]:


u=Matrix([[-915, 1002, 1213]])
v =Matrix([[1180, 1218, 1015]])


# In[49]:


p = (u.cross(v))
p


# In[59]:


a=p[:1]
b=p[1:2]
c=p[2:]
print(a)
print(b)
print(c)


# In[70]:


s = abs(((sqrt(((-460404)**2+(2360065)**2+(-2296830)**2)))/2).evalf())
round(s)


# Ответ: 1662626

# Найдите величину угла в радианах между плоскостью 

# In[75]:


from math import sqrt, acos, degrees
 
x1 = -724
y1 = 1166
z1 = -732
 
x2 = 1007
y2 = -964
z2 = -933
 
def scalar(x1, y1, z1, x2, y2, z2):
    return x1*x2 + y1*y2 + z1*z2
 
def module(x, y, z):
    return sqrt(x ** 2 + y ** 2 + z ** 2)
 
cos = scalar(x1, y1, z1, x2, y2, z2)/(module(x1,y1,z1)*module(x2,y2,z2))
 
ang = acos(cos)
 
print(round(degrees(acos(cos))))


# In[ ]:




