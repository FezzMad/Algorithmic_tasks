def remains(number, current):
    return number - current

def isSquare(number):
    for num in range(0, number//2):
        if num * num == number:
            return True
    return False

number = int(input())
matrix = [[]]

members = 4

# i = 0
# while 1:
#     for current_main in range(0, number // 2):
#         item = 1
#         number_tmp = number
#         delta = current_main
#         current = current_main
#         flag = False
#         while item != members:
#             if item == 1:
#                 if isSquare(current):
#                     matrix[i].append(current)
#                     item += 1
#                     delta = number_tmp - current
#                 else:
#                     current += 1
#             else:
#                 if isSquare(delta):
#                     matrix.append(delta)
#                     flag = True
#                 else:
#
#             if isSquare(current):
#                 matrix[i].append(delta)
#                 delta = number - current
#
#
#     i += 1
