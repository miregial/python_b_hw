from math import gcd
class Frac:

    # n - numerator (числитель)
    # d - denominator (знаменатель)
    def __init__(self, n, d):
        if(d == 0):
            raise ZeroDivisionError
        t = gcd(n, d)
        self.n = n // t
        self.d = d // t

    # разность между «самим» объектом (self) и каким-то иным (other)
    def __sub__(self, other):
        return Frac(self.n * other.d - other.n * self.d, self.d * other.d)

    # представление объекта в виде строки
    def __repr__(self):
        return f"{self.n}/{self.d}"

a = Frac(1,2)
b = Frac(2,6)
print(f"{a} - {b} = {a-b}")
#c = Frac(1,0)
