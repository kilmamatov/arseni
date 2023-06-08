from main1 import Parent


class Descendant(Parent):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def sum_z_and_max(self):
        value = self.z**3 + max(self.x, self.y)**3
        return value

    def __del__(self):
        print("Объект удален")


if __name__ == '__main__':
    a = int(input('Целое число X: '))
    b = int(input('Целое число Y: '))
    c = float(input('Вещественное число Z: '))
    result = Descendant(a, b, c)
    print('Sum(z**3 + max(x, y)**3) = ', result.sum_z_and_max())
