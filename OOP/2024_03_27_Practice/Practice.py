# Комплексные числа

class Complex:
    def __init__(self, real, image): # Конструктор
        self.real = real
        self.image = image
    def __add__(self, other): # Сложение
        return Complex(self.real + other.real, self.image + other.image)
    def __sub__(self, other): # Разность
        return Complex(self.real - other.real, self.image - other.image)
    def __mul__(self, other): # Умножение
        return Complex(self.real * other.real - self.image * other.image, self.real * other.image + self.image * other.real)
    def __truediv__(self, other):
        divisor = other.real ** 2 + other.image ** 2
        real = (self.real * other.real + self.image * other.image)/divisor
        image = (self.image * other.real - self.real * other.image)/divisor
        # print(divisor, (self.real * other.real + self.image * other.image), (self.image * other.real - self.real * other.image))
        return Complex(real, image)
    def __str__(self): # Вывод
        return f'{self.real} {"+" if self.image >= 0 else "-"} {abs(self.image)}'

num1 = Complex(4,3)
num2 = Complex(2, -6)
print(num1 + num2)
print("Number1 - ", num1)
print("Number2 - ", num2)
print("Разность - ", num1 - num2)
print("Деление - ", num1 / num2)
print("Сумма - ", num1 + num2)
print("Умножение - ", num1 * num2)

