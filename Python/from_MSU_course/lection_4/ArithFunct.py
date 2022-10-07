# Арифметика функций
#
# Написать четыре функции (функционала): ADD(f, g), SUB(f, g), MUL(f, g) и DIV(f, g),
# параметрами которых могут быть как обычные объекты, так и функции от одной переменной
# (проверить, является ли объект функцией можно с помощью callable(объект)).
# Возвращать эти функционалы должны функцию от одной переменной h(x), которая выполняет соответствующее действие —
# f(x)+g(x), f(x)-g(x), f(x)*g(x) или f(x)/g(x) — над этими переменными.
# Если f или g не были функцией, вместо f(x) используется f,
# а вместо g(x) — g (например, при умножении функции на константу).
#
# Примеры
#   Входные данные
#       from math import *
#
#       f = SUB(sin, cos)
#       print(f(12), sin(12)-cos(12))
#
#       g = DIV(sin, cos)
#       print(g(pi/6), tan(pi/6))
#
#       h = MUL(exp, 0.1)
#       print(h(2), e**2/10)
#
#       t = ADD(len, sum)
#       print(t(range(5)))

#   Результат работы
#       -1.380426876732927 -1.380426876732927
#       0.5773502691896256 0.5773502691896257
#       0.7389056098930651 0.738905609893065
#       15




def ADD(f, g):
    def h(x):
        if callable(f) and callable(g):
            return f(x) + g(x)
        elif callable(f):
            return f(x) + g
        elif callable(g):
            return f + g(x)
        else:
            return f + g
    return h


def SUB(f, g):
    def h(x):
        if callable(f) and callable(g):
            return f(x) - g(x)
        elif callable(f):
            return f(x) - g
        elif callable(g):
            return f - g(x)
        else:
            return f - g
    return h


def MUL(f, g):
    def h(x):
        if callable(f) and callable(g):
            return f(x) * g(x)
        elif callable(f):
            return f(x) * g
        elif callable(g):
            return f * g(x)
        else:
            return f * g
    return h

def DIV(f, g):
    def h(x):
        if callable(f) and callable(g):
            return f(x) / g(x)
        elif callable(f):
            return f(x) / g
        elif callable(g):
            return f / g(x)
        else:
            return f / g
    return h