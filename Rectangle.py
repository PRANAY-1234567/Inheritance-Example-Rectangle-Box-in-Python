class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def input_dimensions(self):
        self.length = float(input("Enter the length : "))
        self.breadth = float(input("Enter the breadth : "))

    def area(self):
        a = self.length * self.breadth
        print("Area of rectangle :", a)

    def perimeter(self):
        p = 2 * (self.length + self.breadth)
        print("Perimeter of rectangle :", p)


class Box(Rectangle):   # Inheriting Rectangle class
    def __init__(self):
        super().__init__()
        self.height = 0

    def input_height(self):
        self.height = float(input("Enter the height : "))

    def volume(self):
        v = self.length * self.breadth * self.height
        print("Volume :", v)

    def surface_area(self):
        sa = 2 * self.length * self.height + 2 * self.length * self.breadth + 2 * self.breadth * self.height
        print("Surface Area :", sa)


class Inh2:
    @staticmethod
    def main():
        box = Box()

        box.input_dimensions()
        box.input_height()

        print("\n\nBase of Box")
        print("--------------------")
        box.area()
        box.perimeter()

        print("\n\nBody of Box")
        print("--------------------")
        box.volume()
        box.surface_area()


# Calling main method
Inh2.main()