import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        diff_in_x = self.__x - x
        diff_in_y = self.__y - y
        return math.hypot(diff_in_x, diff_in_y)

    def distance_from_point(self, point):
        diff_in_x = self.__x - point.getx()
        diff_in_y = self.__y - point.gety()
        return math.hypot(diff_in_x, diff_in_y)