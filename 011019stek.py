#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Stack:                    #Односимвольно
    """
    Реализация стека на базе вектора
    (для языка Python она тривиальна)
    """

    def __init__(self):          #конструктор создания списка
        self.array = []

    def push(self, c):           #метод экземпляра
        self.array.append(c)     #добавляем к списку элемент 

    def pop(self):               #изъятие из стека последнего значения
        return self.array.pop()  #[1,2].pop = 2

    def top(self):               #показывает содержание списка
        return self.array[len(self.array) - 1]


if __name__ == "__main__":      #Показывает стек в виде словаря ,Вырезая значение 2
    s = Stack()
    print(s.__dict__)
    s.push(1)
    s.push(2)
    print(s.__dict__)
    a = s.pop()
    print(f"a={a}, array={s.__dict__}") 


# In[13]:


#!/usr/bin/env python3 - шибант = запускалка на линуксе для автоматического запуска
#компилятор форм - компф
import re
#from stack import Stack


class Compf(Stack):                                   #потомок класска стэк и все методы поп топ будут из родительскоо класса
    """
    Стековый компилятор формул преобразует правильные
    арифметические формулы (цепочки языка, задаваемого
    грамматикой G0) в программы для стекового калькулятора
    (цепочки языка, определяемого грамматикой Gs):

    G0:
        F  ->  T  |  F+T  |  F-T                     # ф- форма,  т - терм,  в -переменные односимвольные
        T  ->  M  |  T*M  |  T/M
        M  -> (F) |   V
        V  ->  a  |   b   |   c   |  ...  |    z

    Gs:
        e  ->  e e + | e e - | e e * | e e / |       #Обратная польская нотация
                     | a | b | ... | z
    В качестве операндов в формулах допустимы только
    однобуквенные имена переменных [a-z]
    """

    def __init__(self):
        # Инициализация (конструктор) класса Stack
        super().__init__()                           #в классе стек смотрим как создается объект - пусктым списком
        # Создание массива с результатом компиляции
        self.data = []

    def compile(self, str):                          #метод экзмепляра и мы коспилируем строчку
        self.data.clear()                            #очтищение списка - полностью пустой
        # Последовательный вызов для всех символов
        # взятой в скобки формулы метода process_symbol
        for c in "(" + str + ")":
            self.process_symbol(c)
        return " ".join(self.data)

    # Обработка символа
    def process_symbol(self, c):
        if c == "(":                                   #открыли стек
            self.push(c)
        elif c == ")":                                #вытаскиваем ее из стека
            self.process_suspended_operators(c)
            self.pop()
        elif c in "+-*/":                             #если с входит в эти операции
            self.process_suspended_operators(c)
            self.push(c)                              #в стек кладем только скобки и процессы
        else:
            self.check_symbol(c)
            self.process_value(c)

    # Обработка отложенных операций
    def process_suspended_operators(self, c):       #операция предшествования - перед открывающей скобкой - ничего 
        while self.is_precedes(self.top(), c):      #и после закрытой скобки - ничего
            self.process_oper(self.pop())

    # Обработка имени переменной
    def process_value(self, c):
        self.data.append(c)

    # Обработка символа операции
    def process_oper(self, c):
        self.data.append(c)

    # Проверка допустимости символа
    @classmethod
    def check_symbol(self, c):
        if not re.compile("[a-z]").match(c):
            raise Exception(f"Недопустимый символ '{c}'")

    # Определение приоритета операции
    @staticmethod
    def priority(c):
        return 1 if (c == "+" or c == "-") else 2

    # Определение отношения предшествования
    @staticmethod
    def is_precedes(a, b):
        if a == "(":
            return False
        elif b == ")":
            return True
        else:
            return Compf.priority(a) >= Compf.priority(b)


if __name__ == "__main__":
    c = Compf()
    while True:
        str = input("Арифметическая  формула: ")
        print(f"Результат её компиляции: {c.compile(str)}")
        print()


# In[ ]:


#!/usr/bin/env python3
# калькулятор для односимвольных
import re
from operator import add, sub, mul, truediv
#from stack import Stack
#from compf import Compf


class Calc(Compf):                                                  #дочерний класс комфа
    """ 
    Интерпретатор арифметических выражений вычисляет значения
    правильных арифметических формул, в которых в качестве
    операндов допустимы только цифры [0-9]
    """

    def __init__(self):
        # Инициализация (конструктор) класса Compf
        super().__init__()
        # Создание стека для работы стекового калькулятора
        self.s = Stack()

    # Интерпретация арифметического выражения
    def compile(self, str):
        Compf.compile(self, str)
        return self.s.top()

    # Обработка цифры
    def process_value(self, c):
        self.s.push(int(c))

    # Обработка символа операции
    def process_oper(self, c):
        second, first = self.s.pop(), self.s.pop()
        self.s.push({"+": add, "-": sub, "*": mul,
                     "/": truediv}[c](first, second))

    # Проверка допустимости символа
    @classmethod
    def check_symbol(self, c):
        if not re.compile("[0-9]").match(c):
            raise Exception(f"Недопустимый символ '{c}'")


if __name__ == "__main__":
    c = Calc()
    while True:
        str = input("Арифметическое выражение: ")
        print(f"Результат его вычисления: {c.compile(str)}")
        print()


# In[ ]:


понять что за методы и к чему они и тесты проработать


# In[ ]:




