# 원의 둘레와 넓이를 구하는 객체 지향 프로그램
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.radius
    def get_area(self):
        return math.pi * (self.radius ** 2)
    
# 원의 둘레와 넓이를 구합니다.
circle = Circle(10)
print("원의 둘레: {:.3f}".format(circle.get_circumference()))
print("원의 넓이: {:.3f}".format(circle.get_area()))