from math import *


def f14(n):
    if n == 0:
        return 4
    elif n == 1:
        return 2
    else:
        return sin(f14(n - 2)) - fabs(f14(n - 2)) - 26


float(f14(16))