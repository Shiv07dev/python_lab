from math import pi

def area(r):
    result = pi * r * r
    return result

import __main__ as Rajkot   # using alias in same file

r = int(input("Enter radius: "))
result = Rajkot.area(r)
print("After calculation, area is:", result)