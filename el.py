# -*- coding: utf-8 -*-
"""
Created on Thu Mar 07 15:29:26 2019

@author: B18-702
"""


from turtle import *
import time

def tree(size):          # елка
    if size < 2:
        return 
        # часть ствола
    fd(size*0.2) 
    # повернулись и рекурсивно: правая ветвь
    right(110); tree(size*0.4)
        # повернулись и продвинулись вверх
    left(110); fd(size*0.1)
    left(110); tree(size*0.4)
    
    right(110)
    tree(size*0.7)
    bk(size*0.3) 

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
to_start(0, -100)
tree(800)
exitonclick()     