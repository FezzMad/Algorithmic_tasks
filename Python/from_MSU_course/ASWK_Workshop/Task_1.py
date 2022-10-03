# Задача_1 (в решении должен быть хотя бы один оператор if)
#
# заданы три класса чисел:
#   A: четные, делящиеся на 25
#   B: нечетные, делящиеся на 25
#   C: делящиеся на 8
# напишите программу, которая:
#   вводит целое число
#   выводит информацию о его принадлежности к классам A, B, C
#   формат вывода: "A - B + C +" (через пробел)
#
#   Ввод
#       125
#   Вывод
#       A - B + C -

def isDiv8(num):
    return not (num % 8)


def isDiv25(num):
    return not (num % 25)


def isEven(num):
    return not (num % 2)


def isA(num):
    return isEven(num) and isDiv25()


def isB(num):
    return not isEven(num) and isDiv25(num)


def isC(num):
    return isDiv8(num)


def task_1(num):
    a, b, c = "-", "-", "-"
    if (isA(num)):
        a = "+"
    if (isB(num)):
        b = "+"
    if (isC(num)):
        c = "+"
    return "A " + a + " B " + b + " C " + c


def test_task_1(num, output):
    if task_1(num) == output:
        print("OK")
    else:
        print("NA")


num = int(input())
print(task_1(num))


