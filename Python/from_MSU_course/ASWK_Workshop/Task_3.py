# Задача_3 (в решении должны использоваться вложенные циклы while)
#
# напишите программу, которая:
#   вводит целое положительное число N
#   выводит таблицу умножения целых чисел от N до N+2 в виде таблицы 3x3
#       n * n = ... n * (n+1) = ... n * (n+2) = ...
#       (n+1) * n = ... (n+1) * (n+1) = ... (n+1) * (n+2)= ...
#       (n+2) * n = ... (n+2) * (n+1) = ... (n+2) * (n+2)= ...
#   форматировать столбцы, чтобы они были "ровными" (т.е. выравнивать длину примеров), не нужно
#   при этом если сумма цифр произведения равна 6, то вместо результата печатать смайлик :=)
#
# последовательности python (в частности, строки для подсчета суммы цифр), конструкцию range()
# и форматные строки при написании программы использовать нельзя
#
#   ввод
#       4
#   вывод
#       4 * 4 = 16 4 * 5 = 20 4 * 6 = :=)
#       5 * 4 = 20 5 * 5 = 25 5 * 6 = 30
#       6 * 4 = :=) 6 * 5 = 30 6 * 6 = 36

def sumNumbers(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum


def task_3(num):
    ans = ""
    for n in range(num, num + 3):
        for m in range(num, num + 3):
            solve = ""
            if sumNumbers(prod := n * m) == 6:
                solve = ":=)"
            else:
                solve = prod
            ans += f"{n} * {m} = {solve} "
        ans += '\n'
    return ans


def test_task_3(num, output):
    if task_3(num) == output:
        print("OK")
    else:
        print("NA")


num = int(input())
print(task_3(num))
