class Bird():
  #  def __init__(self):

    def fly(self): #метод класса (текущий объект)
        #print(f"Я прица породы {type(self)}, я - лечу.")
        print(f"Я прица породы {self.__class__.__name__}, я - лечу.") #форматная строка f"2+2={2+2}" нижние подчеркивания-имя класса
b = Bird()
b.fly()


class Parrot(Bird): #подметод - дочерний
    def __init__(self, name = "Петя"): #экземпляр класса м параметр по умолчанию
        self.name = name
    def say(self):
        print(f"Меня зовут {self.name}.")

p = Parrot()
p.fly()
p.say()

p2 = Parrot("Умница-говорун")
p2.say()

class Pinguin(Bird):
      def fly(self):
        print(f"Я прица породы {self.__class__.__name__}, я - не летаю (пока не пнёшь).")


p3 = Pinguin()
#p3.say()
p3.fly()
