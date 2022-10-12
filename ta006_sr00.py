#!/usr/bin/env python
# coding: utf-8

# # Знакомство с SymPy

# ### Самостоятельная работа

# ### Тулеубаева Айгерим  (ta006), группа: Б18-702

# **Выполните указанные ниже действия, сохраните свою работу в виде ipynb-файла с именем `ta006_sr00.ipynb` и прикрепите этот файл к сообщению своему преподавателю**.

# **Задание 1.** Постройте график той первообразной функции $(4x+7)^2(3x-11)^3$, которая в точке $x_0=-2$ принимает значение $y_0=19992$.

# In[75]:


from sympy import *
init_printing()
#var('x y ')
#a=integrate(((4*x+7)**2)*((3*x-11)**3),x)
def f(x):
    y = (((4*x+7)**2)*((3*x-11)**3))
    i = integrate( y, x) #(((4*x+7)**2)*((3*x-11)**3)
#a=integrate(((4*x+7)**2)*((3*x-11)**3),x)
    return i #integrate(((4*x+7)**2)*((3*x-11)**3),x
#f(-2,19992)
    #y = ((4*x+7)**2)*((3*x-11)**3)
    #i = integrate(p)
    #print(i)
plotting.plot3d(i)
print(i)
#f(-2,19992)


# In[8]:


#a=integrate(((4*x+7)**2)*((3*x-11)**3),x)
#plotting.plot3d(x**2+y**2, (x,-3,3), (y,-3,3))


# **Задание 2.** Найдите площадь треугольника, построенного на векторах $\vec{u} = (-915,1002,1213)$ и $\vec{v} = (1180,1218,1015)$.
# Завершите решение созданием (вручную) ячейки типа `Markdown`,
# в которой полученному ответу, округлённому до целого числа,
# предшествует текст «`Ответ:`»

# In[ ]:





# **Задание 3.** Найдите величину угла в радианах между плоскостью $\displaystyle \pi\colon -724x + 1166y - 732z - 748 = 0$ и прямой $\displaystyle l\colon \left\{\begin{array}{l}
# x(t) = 1007t - 1256\\
# y(t)=-964t + 1190\\
# z(t)=-933t + 1151
# \end{array}\right.$.
# Завершите решение созданием (вручную) ячейки типа `Markdown`,
# в которой полученному ответу, округлённому до сотых,
# предшествует текст «`Ответ:`»

# In[ ]:



