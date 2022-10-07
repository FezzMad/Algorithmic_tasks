# Подсчёт кратных
# Написать функцию moar(a, b, n) от трёх параметров — целочисленных последовательностей a и b, и натурального числа n. Функция возвращает True, если в a больше чисел, кратных n, чем в b, и False в противном случае.
#
# Примеры
#   Входные данные
#       print(moar((25,0,-115,976,100500,7),(32,5,78,98,10,9,42),5))
#
#   Результат работы
#       True


def count(a, n):
    count = 0
    for num in a:
        if num % n == 0:
            count += 1
    return count


def moar(a, b, n):
    count_a = count(a, n)
    count_b = count(b, n)
    return count_a > count_b