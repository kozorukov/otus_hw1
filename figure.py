import math


class Figure:
    def __init__(self, name, angles):
        self.name = name
        self.angles = angles

    def my_name(self):
        print(f"My name's {self.name}!")
        return self.name

    def my_angles(self):
        print(f"I've {self.angles} angles!")
        return self.angles


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        super().__init__(name, 3)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        p = self.a + self.b + self.c
        print(f"Perimeter = {p}!")
        return p

    def area(self):
        pp = (self.a + self.b + self.c) / 2
        s = math.sqrt(pp*(pp - self.a)*(pp - self.b)*(pp - self.c))
        print(f"Area is {s}!")
        return s


class Rectangle(Figure):
    def __init__(self, name, a, b):
        super().__init__(name, 4)
        self.a = a
        self.b = b

    def perimeter(self):
        p = (self.a + self.b) * 2
        print(f"Perimeter = {p}!")
        return p

    def area(self):
        s = self.a * self.b
        print(f"Area is {s}!")
        return s



class Square(Figure):
    def __init__(self, name, a):
        super().__init__(name, 4)
        self.a = a

    def perimeter(self):
        p = self.a * 4
        print(f"Perimeter = {p}!")
        return p

    def area(self):
        s = self.a ** 2
        print(f"Area is {s}!")
        return s


class Circle(Figure):
    def __init__(self, name, r):
        super().__init__(name, 0)
        self.r = r

    def area(self):
        s = math.pi * (self.r ** 2)
        print(f"Area is {s}!")
        return s

    def perimeter(self):
        p = 2 * math.pi * self.r
        print(f"Perimeter = {p}!")
        return p



