# Сушинський Ігор
# Лабораторна робота №5
# Функції

from funcs_module import *

a = int(input("Введіть початок проміжку: a = "))
b = int(input("Введіть кінець проміжку: b = "))
h = int(input("Введіть крок проміжку: h = "))

y1 = "2 * (x ** 2 - 3) - (sin(x) ** 2 / (1 + cos(x))) + cos(abs(x)) ** 2 - log(abs(x) + 2) - 1 + sin(x) ** 2"
y2 = "7 - 4 * x - x ** 2 + x ** 3 + log(3 + 2 * abs(x)) + 1 / tan((4 + abs(x)) / 8) + sqrt(1 - sin(x) ** 2)"

result1 = calculate_expression(y1, a, b, h)
result2 = calculate_expression(y2, a, b, h)

print(f"Варіант 18: {result1}")
print(f"Варіант 38: {result2}")
