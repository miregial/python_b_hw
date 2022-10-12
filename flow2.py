# -*- coding: utf-8 -*-
"""
Created on Thu Mar 07 15:05:01 2019

@author: B18-702
"""


from turtle import *
import time

def flower(len):  # рисунок
    fd(2*len), right(30)
    for k in range(11):
        fd(len); bk(len); left(6)
    
    right(36); bk(2*len)

def increase(len):   # анимация
    if len > 200:
        return 
    clear()          # стерли
    flower(len)      # нарисовали
    time.sleep(0.01) # подождали
    increase(len+2)  # рекурсия !!!

tracer(8, 25)        # ускоряет процесс рисования
width(2)
ht()
bgcolor('#4d000d')
pencolor('#f0bb90')  
left(90); bk(250)   # спустились пониже
pd()

#flower(200)
increase(60)
exitonclick() 