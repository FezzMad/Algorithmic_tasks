matrix = []
while inp := input():
    matrix.append(eval(inp))

new_matrix = []
for i in range(0, len(matrix)):
    list = []
    for j in range(0, len(matrix[0])):
        if j <= i:
           list.append(matrix[i][j])
    new_matrix.append(list)

for i in range(1, len(matrix)):
    for j in range(len(matrix[0]) - 1, -1, -1):
        new_matrix[i].append(matrix[j][i])

for list in new_matrix:
    for element in list:
        print(element, end=",")
    print()

