class Polygon:
    def input_sides(self):
        self.sides = []
        n = int(input("Enter the number of sides: "))

        for i in range(n):
            side = float(input(f"Enter side {i + 1}: "))
            self.sides.append(side)

    def display_sides(self):
        print("Sides of the polygon are:", self.sides)


class Triangle(Polygon):
    def area(self):
        a, b, c = self.sides

        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        print("Area of the triangle:", area)


t = Triangle()

t.input_sides()
t.display_sides()
t.area()
