from deq import Deq
from r2point import R2Point


class Figure:
    """ Абстрактная фигура """

    p1 = None
    p2= None
    p3 = None
    dist  = None


    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0


    #def minotrezok(self):
        #return 0

    #def dliny(self):
        #return 0

class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        #return self if self.p == q else Segment(self.p, q)
        if self.p != q:
            Figure.p1 = self.p
            Figure.p2 = q
            Figure.dist = self.p.dist(q)
            return Segment(self.p, q)
        else:
            return self


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    #def minotrezok(self):
        #return self.p.dist(self.q)

    #def dliny(self):
        #return self.p.dist(self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            Figure.dist = min(self.p.dist(self.q) , self.p.dist(r), self.q.dist(r))
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            Figure.p1 = self.p
            Figure.p2 = r
            Figure.dist = self.p.dist(r)
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            Figure.p1 = r
            Figure.p2 = self.q
            Figure.dist = r.dist(self.q)
            return Segment(r, self.q)
        else:
            return self




class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))


    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    #def minotrezok(self):
        #return self._minotrezok

    #def dliny(self):
        #return self._dliny

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):
            Figure.dist =
            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))


            #self._dliny = list([a.dist(b), b.dist(c),  c.dist(a)])
            #self._minotrezok = min(self._dliny)

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                #self._minotrezok -= p.dist(self.points.first())
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                #self._minotrezok -= p.dist(self.points.last())
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            self.points.push_first(t)

        return self


if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
