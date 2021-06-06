from math import *


def f1(x, y, z):
    return sqrt(57*x**7-37*x**6) + y**4 + sin(y**4) + 19 + sqrt((48*z**7 - tan(x) - 68)/(z**2+96*x**7))


print(f1(37, 17, 37))