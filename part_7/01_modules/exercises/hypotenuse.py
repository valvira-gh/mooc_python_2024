import math

def hypotenuse(leg1: float, leg2: float):
    # Pythagoras theorem a² + b² = c²
    c = math.sqrt(leg1 ** 2 + leg2 ** 2)
    return float(c)


print(hypotenuse(3,4))
print(hypotenuse(5,12))