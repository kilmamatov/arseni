class Parent:
    def __init__(self, x, y):  # базовый конструктор классов
        self.x = x  # создаем переменную
        self.y = y

    def cube(self):  # функция
        value = max(self.x, self.y)**3  # получаем максимальный аргумент ввозведенную в куб
        return value

    def info(self):  # функция информации о классе
        s = f'Целое число X: {self.x}\nЦелое число Y: {self.y}'  # переменная содержащая стоку со значениями
        return s


if __name__ == '__main__':  # скрипт на запуск с заданнами параметрами
    a = int(input('Целое число X: '))
    b = int(input('Целое число Y: '))
    result = Parent(a, b)  # создали переменную класса
    print(f'Куб большего из чисел = {result.cube()}')
