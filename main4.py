import math
from main2 import Coordinates


class Triangle(Coordinates):
    def __init__(self, x1, x2, y1, y2, x3, y3):  # базовый конструктор класса
        super().__init__(x1, x2, y1, y2)  # базовая фукция супер для переопределения переменных в родительский класс
        self.x3 = x3  # создаем переменную
        self.y3 = y3  # создаем переменную

    def area_of_a_triangle(self):
        a = abs(math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2))  # получаем первую сторону треугольника
        b = abs(math.sqrt((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2))  # получаем вторую сторону треугольника
        c = abs(math.sqrt((self.x1 - self.x3)**2 + (self.y1 - self.y3)**2))  # получаем третью сторону треугольника
        p = (a + b + c) / 2  # получаем полупириметр
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))  # получаем площадь по формуле с полупириметром
        return s


if __name__ == '__main__':
    print('Введите координаты')
    num_x1 = int(input('x1: '))
    num_x2 = int(input('x2: '))
    num_y1 = int(input('y1: '))
    num_y2 = int(input('y2: '))
    num_x3 = int(input('x3: '))
    num_y3 = int(input('y3: '))
    result = Triangle(num_x1, num_x2, num_y1, num_y2, num_x3, num_y3)
    print('Площадь треугольника', result.area_of_a_triangle())

