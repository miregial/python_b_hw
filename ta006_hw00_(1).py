#!/usr/bin/env python
# coding: utf-8

# # Знакомство с SymPy

# ### Индивидуальное домашнее задание

# ### Тулеубаева Айгерим  (ta006), группа: Б18-702

# **Выполните указанные ниже действия, сохраните свою работу в виде ipynb-файла с именем `ta006_hw00.ipynb` и прикрепите этот файл к сообщению своему преподавателю**.

# **Задание 1.** Вычислите значение выражения $\displaystyle\ln\left(\frac{\sqrt[3]{\ln2}}{(3-e){(\cos3 + 5)}^2}\right)$ с точностью 40 значащих десятичных цифр.

# In[1]:


from sympy import *
init_printing()
f = ln(((ln(2))**(1/3))/((3-E)*(cos(3)+5)**2))
#z1=S(f)/1; z1
#z2=z1.n(40); z2 # вычисляет переменную z2 с точностью до 40 значащих цифр
f.evalf(40) 


# **Задание 2.** Раскройте скобки в выражении $\left(u + z\right)^{2} \left(x - 2 y\right)^{3} \left(x + 2 y\right)^{3}$.

# In[2]:


from sympy import *
init_printing()
var ('u,z,x,y')
f=((u+z)**2)*((x-2*y)**3)*((x+2*y)**3)
expand(f)


# **Задание 3.** Разложите на множители многочлен $4 u^{2} x z^{2} - 12 u^{2} x z + 9 u^{2} x - 8 u^{2} y z^{2} + 24 u^{2} y z - 18 u^{2} y + 8 u x z^{3} - 24 u x z^{2} + 18 u x z - 16 u y z^{3} + 48 u y z^{2} - 36 u y z + 4 x z^{4} - 12 x z^{3} + 9 x z^{2} - 8 y z^{4} + 24 y z^{3} - 18 y z^{2}$.

# In[3]:


var('u,x,z,y')
f  =  (4*u**2*x*z**2)-(12*u**2*x*z)+(9*u**2*x)-(8*u**2*y*z**2)+(24*u**2*y*z)-(18*u**2*y)+(8*u*x*z**3)-24*u*x*z**2+18*u*x*z-16*u*y*z**3+48*y*u*z**2-36*u*y*z+4*x*z**4-12*x*z**3+9*x*z**2-8*y*z**4+24*y*z**3-18*y*z**2
factor(f)


# **Задание 4.** Найдите действительные корни уравнения $9 x^{4} + 21 x^{3} + 4 x^{2} - 94 x - 336 = 0$.

# In[4]:


from sympy import *
x = symbols('x', real=True)
solve(9*x**4+21*x**3+4*x**2-94*x-336)


# **Задание 5.** Постройте график функции, заданной неявно: $4y^2-4x^2y-x^5=0$. Используйте одинаковый масштаб по координатным осям.

# In[33]:


from sympy import *
get_ipython().run_line_magic('matplotlib', 'inline')
var('x y')
(x, y)
#plot_implicit(Eq(4*y**2-4*x**2*y-x**5, 0))
#f=Eq(4*y**2-4*x**2*y-x**5, 0) 
p = plot_implicit(4*y**2-4*x**2*y-x**5)


# In[ ]:




