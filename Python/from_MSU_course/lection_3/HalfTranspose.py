# Ввели N строк по N целых чисел (для удобства представлены тут цифрами). Полученную матрицу
#
#   1234
#   5678
#   9012
#   3456
#
# попытались «транспонировать на 45°» — получилось примерно так:
#
#      1
#     5 2
#    9 6 3
#   3 0 7 4
#    4 1 8
#     5 2
#      6
#
# При этом способе поворота между числами образовались «пустые места» каждое размеров в одно число, размер матрицы увеличился до 2N-1 × 2N-1. Затем все числа «упали на свободные места под ними» — переместились до ближайшей незанятой ячейки:
#
#       1
#      562
#     90173
#    3456284
#
# Ввести построчно через запятую элементы исходной квадратной матрицы. Вывести построчно через запятую элементы получившейся матрицы (без учёта свободных ячеек)
#
#
#   1,2,3,4
#   5,6,7,8
#   9,0,1,2
#   3,4,5,6
#
# Для простоты восприятия все числа здесь представлены цифрами, в тестах будут и другие.
#
#
#   1
#   5,6,2
#   9,0,1,7,3
#   3,4,5,6,2,8,4


def below_diagonal(matrix):
    left_half_matrix = []
    for i in range(0, len(matrix)):
        list = []
        for j in range(0, len(matrix[0])):
            if j <= i:
                list.append(matrix[i][j])
        left_half_matrix.append(list)
    return left_half_matrix


def above_diagonal(matrix):
    right_half_matrix = []
    for i in range(0, len(matrix)):
        list = []
        for j in range(0, len(matrix[i])):
            if j > i:
                list.append(matrix[i][j])
        right_half_matrix.append(list)
    return right_half_matrix


def reverse_matrix(matrix):
    for line in matrix:
        line.reverse()


def plus(first_matrix, second_matrix):
    for i in range(0, len(first_matrix)):
        for j in range(0, len(second_matrix[i])):
            first_matrix[i].append(second_matrix[i][j])


def int_matrix_to_str(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = str(matrix[i][j])


matrix = [eval(input())]
size = len(matrix[0]) if type(matrix[0]) is tuple else len(matrix)
i = 1
while i < size:
    i += 1
    matrix.append(eval(input()))

if len(matrix) > 1:

    left_half_matrix = below_diagonal(matrix)
    right_half_matrix = above_diagonal(matrix)

    buf_matrix = [[] for i in range(len(matrix))]

    k = 0
    for i in range(0, len(right_half_matrix)):
        for j in range(0, len(right_half_matrix[i])):
            k = i + j + 1
            buf_matrix[k].append(right_half_matrix[i][j])
        k = 0

    reverse_matrix(buf_matrix)
    plus(left_half_matrix, buf_matrix)
    int_matrix_to_str(left_half_matrix)

    for line in left_half_matrix:
        print(",".join(line))
else:
    print("".join(str(matrix[0])))

