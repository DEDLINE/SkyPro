import math


def square(side):
    return side * side


side = float(input("Введите число: "))
result = square(side)
print(f"Площадь квадрата: {math.ceil(result)}")
