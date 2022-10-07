# Функция побольше
#
# Написать функцию maxfun(), которая принимает переменное число параметров — числовую последовательность S, функцию F1 и, возможно, ещё несколько функций F2 … Fn. Возвращает она ту из функций Fi, сумма значений которой на всех элементах S наибольшая. Если таких функций больше одной, возвращается Fi с наибольшим i.
#
# Примеры
#   Входные данные
#       from math import *
#       print(maxfun(range(-2,10), sin, cos, exp)(1))
#
#   Результат работы
#       2.718281828459045


def reverse_max(seq):
    tmp_seq = list(seq)
    max_num = max(tmp_seq)
    tmp_seq.reverse()
    index = tmp_seq.index(max_num)
    return len(seq) - index - 1


def sum_fun(seq, fun):
    sum = 0
    for elem in seq:
        sum += fun(elem)
    return sum


def maxfun(seq, *funs):
    list = []
    for cur_fun in funs:
        list.append(sum_fun(seq, cur_fun))
    index = reverse_max(list)
    return funs[index]