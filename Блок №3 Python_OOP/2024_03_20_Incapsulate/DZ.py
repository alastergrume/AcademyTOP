from math import pi

class Square:
    def __init__(self, lenght):
        self.lenght = lenght
    def area(self):
        return self.lenght ** 2


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2

class CircleInSquare(Circle, Square):
    def __init__(self, radius):
        Circle.__init__(self, radius)
        Square.__init__(self, radius * 2 ** 0.5)
    def display_details(self):
        print(f"Circle radius: {self.radius}")
        print(f"Square lenght: {self.lenght}")

    def total_area(self):
        circle_area = Circle.area(self)
        square_area = Square.area(self)
        return circle_area, square_area

circle_in_square = CircleInSquare(5)
circle_in_square.display_details()
circle_area, square_area = circle_in_square.total_area()
print(f'Total area of the circle: {circle_area}')
print(f'Total area of the square: {square_area}')


