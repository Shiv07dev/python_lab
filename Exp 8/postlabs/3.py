import math

def evaluate(x):
    f = math.cos(2*x)
    f1 = -2 * math.sin(2*x)
    f2 = -4 * math.cos(2*x)
    return f, f1, f2

x = math.pi   # given x = π
f, f1, f2 = evaluate(x)

print("f(x)  =", f)
print("f'(x) =", f1)
print("f''(x) =", f2)
