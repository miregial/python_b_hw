from turtle import *
import time

def flower(len):  # рисунок
    fd(2*len), right(30)
    for k in range(11):
        fd(len); bk(len); left(6)
    
    right(36); bk(2*len)

def increase(len):   # анимация
    if len > 260:
        return 
    clear()          # стерли
    flower(len)      # нарисовали
    time.sleep(0.01) # подождали
    increase(len+2)  # рекурсия !!!

tracer(8, 25)        # ускоряет процесс рисования
width(2)
ht()
bgcolor('#ade7b9')
pencolor('#fb7c15')  
left(90); bk(250)   # спустились пониже
pd()

#flower(200)
increase(100)
exitonclick()       # любуемся!