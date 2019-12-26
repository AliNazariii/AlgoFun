import math
a, b, c = map(int, input().split())
delta = math.sqrt((b * b) - 4 * a * c)
x = (-b - delta) / (2 * a)
y = (-b + delta) / (2 * a)
print(str(x) + " " + str(y))