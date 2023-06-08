class Parent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cube(self):
        value = max(self.x, self.y)**3
        return value

    def info(self):
        s = f'Целое число X: {self.x}\nЦелое число Y: {self.y}'
        return s


if __name__ == '__main__':
    a = int(input('Целое число X: '))
    b = int(input('Целое число Y: '))
    result = Parent(a, b)
    print(f'Куб большего из чисел = {result.cube()}')
