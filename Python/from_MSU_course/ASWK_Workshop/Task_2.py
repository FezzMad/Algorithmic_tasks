# Задача_2 (в решении должен использоваться цикл while с клаузой else)
#
# напишите программу, которая:
#   в цикле вводит целые числа
#   суммирует введённые положительные числа
#   если введен 0 или отрицательное число, выводит последнее введенное число и завершает работу
#   если сумма превысила 21, выводит сумму и завершает работу
#
#   ввод
#       4
#       5
#       -100
#   вывод
#       -100
#
#   ввод
#       15
#       16
#   вывод
#       31

def task_2():
    sum = 0
    while num := int(input()):
        if num < 0:
            return num
        sum += num
        if sum > 21:
            return sum
    else:
        return num


def test_task_2(output):
    if task_2() == output:
        print("OK")
    else:
        print("NA")


print(task_2())


