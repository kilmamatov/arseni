import math
import turtle  # библ для работы
import time  # по факту не нужен (для удобства)


class Coordinates:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def info(self):
        return f'Координата x1 = {self.x1}\n' \
               f'Координата x2 = {self.x2}\n' \
               f'Координата y1 = {self.y1}\n' \
               f'Координата y2 = {self.y2}\n'

    def value(self):
        res = abs(math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2))  # получаем модуль вектора
        return res

    def picture(self):  # функция для отрисовки вектора при помощи turtle
        screen = turtle.Screen()
        screen.title("Линия вектора")
        # создание черепахи
        t = turtle.Turtle()
        # настройка черепахи пикселей
        t.width(2)
        # координаты начала и конца вектора
        x1, y1 = self.x1, self.y1
        x2, y2 = self.x2, self.y2
        # переместить черепаху в начало вектора
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        # рисование вектора
        t.goto(x2, y2)
        # закрытие экрана по нажатию на него
        screen.exitonclick()

    def __del__(self):  # дезтруктор
        print("Объект удален")


if __name__ == '__main__':
    print('Введите координаты')
    num_x1, num_x2, num_y1, num_y2 = int(input('x1: ')), int(input('x2: ')), int(input('y1: ')), int(input('y2: '))
    result = Coordinates(num_x1, num_x2, num_y1, num_y2)  # создаем переменнную класса
    print('Длинна вектора = ', result.value())
    print(result.info())
    time.sleep(2)
    result.picture()


