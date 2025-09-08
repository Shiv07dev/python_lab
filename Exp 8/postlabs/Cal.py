# import math

# x = float(input("Enter value of x: "))
# y = 6 * (x**2) + 4 * math.sin(x)
# print("y =", y)


def yes(x):
    y = 6 * x * x + sin(x)
    return y

from math import *
import Cal as rajkot
a = int (input("Enter value of x: "))
result = rajkot.yes(a)
print("After evalution result is " , result)
