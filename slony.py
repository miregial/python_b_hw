from  turtle import *
import random

def el(x, l):
    pu()
    setpos(x,0)
    if x < -350:
        print(x)
        return
    pu()
    for (xi,yi) in pts():
        setpos(x+l*xi, l*yi)
        pd()

    pu();
    setheading(0)
    fd(-1.5*l); lt(90); fd(2*l); pd()
    circle(l/4)
    pu()
    el(x-l*16, l+1)


def pts():
    return [( 1,  5), ( 5,  5), ( 6,  4), ( 7,  3), ( 7,  0),
            ( 7,  3), ( 6,  0), ( 7, -2), ( 6, -3), ( 5, -1),
            ( 5, -3), ( 3, -3), ( 2,  0), ( 5, -1), ( 2,  0),
            ( 1,  0), ( 2, -3), ( 0, -3), (-1,  0), (-1, -3),
            (-3, -3), (-2,  0), (-1,  0), (-2,  0), (-3,  1),
            (-4,  0), (-5, -2), (-6, -3), (-7, -3), (-8, -2),
            (-8, -1), (-7, -2), (-7, -2), (-6, -2), (-5,  0),
            (-5,  2), (-6,  3), (-6,  5), (-4,  7), (-3,  7),
            (-2,  6), (-1,  5), (-1,  6), ( 0,  6), ( 1,  5),
            ( 1,  2), (-1,  1), (-2,  1), (-2,  2), (-3,  1)]


def draw(size):
    x1, y1 = pos()
    pu()
    for (x,y) in pts():
        setpos(x1+x*size,y1+y*size)
        pd()
    pu();
    fd(-1.5*size); lt(90);
    fd(2*size);
    pd()
    circle(size/4)
    heading = 0
    pu()


    def go():
        ht(); draw(5)
pu()
def my_colors():
    return ["red", "yellow", "green"]
def random_el(n):
    for i in range(n):
        pencolor(random.choice(my_colors()) )
        x0 = random.randint(-300, 300)
        y0 = random.randint(-300, 300)
        setpos(x0,y0)
        size = random.randint(10, 50)
        draw(size)
        pu()

pu()
width(3)
random_el(5)
exitonclick()
