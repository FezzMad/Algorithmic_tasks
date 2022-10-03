# Ящик с точками
# Вводить вещественные числа x, y и z по три в строке через запятую, считая их координатами точек (не менее одной тройки). Конец ввода — пустая строка. Вывести минимальный объём параллелепипеда со сторонами, параллельными осям координат, содержащего все точки.
#
# Примеры
#   Входные данные
#       3,2,1
#       -1.5, -1.5, -1.5
#       1,-1.3,1
#       0,0.5,0
#       1,2,3
#   Результат работы
#       70.875

def min_coordinates(x, y, z, x_min, y_min, z_min):
    x_min = min(x, x_min)
    y_min = min(y, y_min)
    z_min = min(z, z_min)
    return x_min, y_min, z_min


def max_coordinates(x, y, z, x_max, y_max, z_max):
    x_max = max(x, x_max)
    y_max = max(y, y_max)
    z_max = max(z, z_max)
    return x_max, y_max, z_max


points = []
while inp := input():
    points.append(eval(inp))

x_max, y_max, z_max = points[0]
x_min, y_min, z_min = points[0]

for point in range(1, len(points)):
    x, y, z = points[point]
    x_max, y_max, z_max = max_coordinates(x, y, z, x_max, y_max, z_max)
    x_min, y_min, z_min = min_coordinates(x, y, z, x_min, y_min, z_min)

x = x_max - x_min
y = y_max - y_min
z = z_max - z_min

print(x * y * z)


