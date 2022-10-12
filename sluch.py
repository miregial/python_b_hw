from  turtle import *
import random

def house_coord():
    return [(2,4), (-2,4), (-2,0), (2,0), (2,4), (0,6), (-2,4)]



def draw_house(size):
    x1, y1 = pos()
    pu()
    for (x,y) in house_coord():
        setpos(x1+x*size,y1+y*size)
        pd()



def go():
    ht(); draw_house(50)


pu()
#go()
def my_colors():
    return ["red", "yellow", "green"]
def random_houses(n):
    for i in range(n):
        pencolor(random.choice(my_colors()) )
        x0 = random.randint(-300, 300)
        y0 = random.randint(-300, 300)
        setpos(x0,y0)
        size = random.randint(10, 50)
        draw_house(size)
        pu()

pu()
width(10)
random_houses(20)
exitonclick()
