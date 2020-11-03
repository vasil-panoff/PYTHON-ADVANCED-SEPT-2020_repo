rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

biggest_sum = 0
best_indexes = (0, 0)

for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + \
                      matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            best_indexes = (i, j)
best_row, best_col = best_indexes

print(f'Sum = {biggest_sum}')
best_matrix = []
row_counter = 0
for r in range(best_row, best_row + 3):
    best_matrix.append([])
    for c in range(best_col, best_col + 3):
        best_matrix[row_counter].append(matrix[r][c])
    row_counter += 1

for row in best_matrix:
    print(" ".join([str(i) for i in row]))