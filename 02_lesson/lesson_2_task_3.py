import math


def square(side):
    return side * side


side = float(input("Введите значение: "))
result = square(side)
print(f"Площадь квадрата: {math.ceil(result)}")
