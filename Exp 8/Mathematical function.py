import math

# 1. pow(x, y)
x = float(input("Enter base (x) for pow: "))
y = float(input("Enter exponent (y) for pow: "))
print("pow(x, y) =", math.pow(x, y))

# 2. sqrt(x)
x = float(input("\nEnter a number for sqrt: "))
print("sqrt(x) =", math.sqrt(x))

# 3. trunc(x)
x = float(input("\nEnter a number for trunc: "))
print("trunc(x) =", math.trunc(x))

# 4. cos(x)
x = float(input("\nEnter angle in radians for cos: "))
print("cos(x) =", math.cos(x))

# 5. sin(x)
x = float(input("\nEnter angle in radians for sin: "))
print("sin(x) =", math.sin(x))

# 6. tan(x)
x = float(input("\nEnter angle in radians for tan: "))
print("tan(x) =", math.tan(x))

# 7. degrees(x)
x = float(input("\nEnter radians for degrees conversion: "))
print("degrees(x) =", math.degrees(x))

# 8. radians(x)
x = float(input("\nEnter degrees for radians conversion: "))
print("radians(x) =", math.radians(x))

# 9. exp(x)
x = float(input("\nEnter a number for exp: "))
print("exp(x) =", math.exp(x))

# 10. log2(x)
x = float(input("\nEnter a number (>0) for log2: "))
print("log2(x) =", math.log2(x))

# 11. log10(x)
x = float(input("\nEnter a number (>0) for log10: "))
print("log10(x) =", math.log10(x))
