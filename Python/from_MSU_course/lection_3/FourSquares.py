# Четыре квадрата
#
# Известно, что любое натуральное число можно представить в виде суммы не более чем четырех квадратов неотрицательных целых чисел (теорема Лагранжа). Ввести натуральное N⩽100000 и найти для него такие целые неотрицательные x,y,z и t, чтобы x²+y²+z²+t²=N. Вывести все такие четвёрки в следующем формате: x,y,z и t — через пробел, и упорядочены по убыванию, а сами четвёрки — лексикографически по возрастанию (без повторений).
#
# Примеры
#   Входные данные
#       100

#   Результат работы
#       5 5 5 5
#       7 5 5 1
#       7 7 1 1
#       8 4 4 2
#       8 6 0 0
#       9 3 3 1
#       10 0 0 0

num = int(input())
root = int(num ** (1 / 2))
one = int(root / 2)
while one <= root:
    two = 0
    while two <= one and one * one + two * two <= num:
        three = 0
        while three <= two and one * one + two * two + three * three <= num:
            ost = two * two + one * one + three * three
            four = int((num - ost) ** (1 / 2))
            if four * four + ost == num and four <= three:
                print(one, two, three, four)
            three += 1
        two += 1
    one += 1