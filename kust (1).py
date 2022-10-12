# -*- coding: utf-8 -*-
"""
Created on Thu Mar 07 15:35:21 2019

@author: B18-702
"""


from turtle import *
import time


def fern(size):       # папоротник
    if size < 5:
        return 
    fd(size/20) 
    left(80);  fern(size*0.3) 
    right(82); fd(size/20) 
    right(80); fern(size*0.3) 
    left(78);  fern(size*0.9) 
    left(4) ;  fd(size/-10) 
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
fern(500)
exitonclick()     