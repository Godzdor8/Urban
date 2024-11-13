import math
from turtledemo.chaos import coosys


class Figure:
    def __init__(self, color: tuple, *args):
        self.sides_count = 0
        self.filled = False
        self.__sides = []
        self.__color = []
        for side in args:
            self.__sides.append(side)
        self.set_color(color[0], color[1], color[2])

    def get_sides(self) -> list:
        return self.__sides

    def get_color(self) -> list:
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        for i in args:
            if i <= 0:
                return False
        return len(args) == len(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color: tuple, *args):
        if len(args) != self.sides_count:
            super().__init__(color, 1)
        else:
            super().__init__(color, *args)

        self.__radius = super().get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

    def get_radius(self):
        return self.__radius

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color: tuple, *args):
        if len(args) != self.sides_count:
            argsl = []
            for i in range(self.sides_count):
                argsl.append(1)
            super().__init__(color, argsl)
        else:
            super().__init__(color, *args)

    def get_square(self):
        sides = super().get_sides()
        p = 0.5 * sum(sides)
        return math.sqrt(p * (p-sides[0]) * (p-sides[1]) * (p-sides[2]))

class Cube(Figure):
    sides_count = 12
    def __init__(self, color: tuple, *args):
        argsl = []
        if len(args) != 1:
            for i in range(self.sides_count):
                argsl.append(1)
        else:
            for i in range(self.sides_count):
                argsl.append(args[0])
        super().__init__(color, *argsl)

    def get_volume(self):
        return super().get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((100, 100, 100), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади треугольника:
print(triangle1.get_square())



