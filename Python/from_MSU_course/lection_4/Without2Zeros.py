# Без двух нулей
# Написать функцию No_2Zero(N, K), которая вычисляет количество N-значных чисел в системе счисления с основанием K, таких что их запись не содержит двух подряд идущих нулей. Лидирующие нули не допускаются. Для EJudge N⩽33.
#
# Примеры
#   Входные данные
#       print(No_2Zero(6, 3))
#
#   Результат работы
#       328


def step(N, K):
    if N == 1:
        return (K - 1, 0, 0)
    elif N > 1:
        b = step(N - 1, K)
        c = (K - 1) * (K ** (N - 1))
        return (c - b[0] - b[1] * K - b[2], b[2] + b[1] * K, b[0])


def No_2Zero(N, K):
    a = step(N, K)
    return a[0] + a[2]