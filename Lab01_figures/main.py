import math

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        p = self.perimeter() / 2
        val = p * (p - self.a) * (p - self.b) * (p - self.c)
        return math.sqrt(val) if val > 0 else 0

class Rectangle:
    def __init__(self, a, b):
        self.a, self.b = a, b
    def perimeter(self): return 2 * (self.a + self.b)
    def area(self): return self.a * self.b

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        if self.a == self.b: return 0
        try:
            term = ((self.b - self.a) ** 2 + self.c ** 2 - self.d ** 2) / (2 * (self.b - self.a))
            h_sq = self.c ** 2 - term ** 2
            return ((self.a + self.b) / 2) * math.sqrt(max(0, h_sq))
        except:
            return 0

class Parallelogram:
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h
    def perimeter(self): return 2 * (self.a + self.b)
    def area(self): return self.a * self.h

class Circle:
    def __init__(self, r):
        self.r = r
    def perimeter(self): return 2 * math.pi * self.r
    def area(self): return math.pi * self.r ** 2


all_figures = []

with open('input01.txt', 'r') as file:
    for line in file:
        parts = line.split()
        if not parts: continue

        name = parts[0]
        p = [float(x) for x in parts[1:]]

        if name == "Triangle":
            all_figures.append(Triangle(p[0], p[1], p[2]))
        elif name == "Rectangle":
            all_figures.append(Rectangle(p[0], p[1]))
        elif name == "Trapeze":
            all_figures.append(Trapeze(p[0], p[1], p[2], p[3]))
        elif name == "Parallelogram":
            all_figures.append(Parallelogram(p[0], p[1], p[2]))
        elif name == "Circle":
            all_figures.append(Circle(p[0]))

best_area_fig = max(all_figures, key=lambda f: f.area())
best_perim_fig = max(all_figures, key=lambda f: f.perimeter())

print(f"Найбільша площа: {best_area_fig.area():.2f}")
print(f"Це фігура: {type(best_area_fig).__name__}")
print("-" * 25)
print(f"Найбільший периметр: {best_perim_fig.perimeter():.2f}")
print(f"Це фігура: {type(best_perim_fig).__name__}")
