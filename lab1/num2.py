import math;


def f12(x):
    if x < 99:
        return 90 * x ** 6 + x ** 4 / 28 - 12
    elif 99 <= x < 191:
        return x ** 2 + x ** 4 + 41
    elif 191 <= x < 228:
        return 94 * x - 25 * x ** 8
    elif 228 <= x < 268:
        return 23 * x ** 6 + x ** 5 / 72 + math.log()
    elif x >= 268:
        return math.exp(x) ** 3 + math.log(x) - 15


f12(220)
