class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * self.pi *  self.radius
circle_1 = Circle(4)
print(circle_1.get_circumference( ))