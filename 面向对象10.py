class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Square(Shape):
    def __init__(self, length):
        super().__init__("正方形")
        self.length = length

    def area(self):
        return self.length * self.length


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("园形")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("三角形")
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


s = Square(5)
c = Circle(6)
t = Triangle(3, 4)
print(s.area())
print(c.area())
print(t.area())
