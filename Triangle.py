from PointsOnaPlane import Point

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points = [vertice1, vertice2, vertice3]

    def perimeter(self):
        side1 = self.__points[0].distance_from_point(self.__points[1])
        side2 = self.__points[1].distance_from_point(self.__points[2])
        side3 = self.__points[2].distance_from_point(self.__points[0])

        return side1 + side2 + side3

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())