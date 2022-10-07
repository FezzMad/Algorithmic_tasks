# Скрытое послание
# Ввести две строки и проверить, содержится ли вторая в первой, с учётом того, что символы второй строки могут находиться в первой на некотором равном расстоянии друг от друга. Вывести YES или NO.
#
#   Примеры
#   Входные данные
#       q-We-Rt-Yu-Iweozzz
#       WRYI

#   Результат работы
#       YES


def index(string, start, char):
    for i in range(start, len(string)):
        if str[i] == char:
            return i
    return -1


def culc_step(first, second):
    return second - first


def answer(string, first, index_start, step):
    list = []
    j = 0
    for i in range(index_start, len(string), step):
        if str[i] != substr[j]:
            break
        list.append(str[i])
        if j == size_substr - 1:
            break
        j += 1
    return "".join(list)


str = input()
substr = input()

size_str = len(str)
size_substr = len(substr)

if size_substr > 0:
    first = substr[0]
    index_first = index(str, 0, first)

    if index_first != -1:
        if size_substr > 1:
            second = substr[1]
            index_second = index(str, index_first + 1, second)

            if index_second != -1:
                step = culc_step(index_first, index_second)

                ans = ''
                while ans != substr and index_first != size_str + 1 - size_substr and index_first != -1 and index_second != -1:
                    ans = answer(str, first, index_first, step)
                    index_first = index(str, index_first + 1, first)
                    index_second = index(str, index_first + 1, second)
                    step = culc_step(index_first, index_second)

                if ans == substr:
                    print("YES")
                else:
                    print("NO")
        else:
            print("YES")
    else:
        print("NO")
else:
    print("YES")



