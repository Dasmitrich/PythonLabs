def func():
    a = 5
    print(a+1,a+2,a+3,a+4, sep='!')
    print(type(a))

    def inner():
        print("Внутренняя функция сработала")
        print(__name__)
    inner()

from math import *
print(cos(60));