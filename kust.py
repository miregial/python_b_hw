# -*- coding: utf-8 -*-
"""
Created on Thu Mar 07 15:35:21 2019

@author: B18-702
"""


from turtle import *
import time

def bush(size, p):  # куст
    if size < p:
        return 
    right(15); fd(size)
    bush(size/1.5, p)
    bk(size); left(15)
    
    left(45); fd(size)
    bush(size/2, p)
    bk(size); right(45)
def to_start(x, y):
    clear()           # очистили от предыдущих изображений
    ht()              # скрыли черепаху
    pu()              # подняли перо
    setpos(x, y)      # переместились в точку (x, y)
    setheading(90)    # черепаха смотрит вверх
    pd()              # опустили перо
tracer(8, 25)
pd()
width(3)
pencolor('darkgreen')
bgcolor('#e1eac0')
to_start(0, -170)
bush(500)
exitonclick()     