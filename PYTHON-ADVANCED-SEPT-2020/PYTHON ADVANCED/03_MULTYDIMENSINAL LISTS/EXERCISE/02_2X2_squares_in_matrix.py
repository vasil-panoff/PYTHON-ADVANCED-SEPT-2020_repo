M, N = tuple(map(int, input().split(' ')))

matrix = [['a'] * N for i in range(M)]

# 3 4
# A B B D
# E B B B
# I J B B

num_squares = 0

for i in range(M):
    row = input().split(' ')

    for j in range(N):
        matrix[i][j] = row[j]

        if matrix[i][j] == matrix[i][j - 1] and \
            matrix[i][j] == matrix[i - 1][j] and \
            matrix[i][j] == matrix[i - 1][j - 1]:
            num_squares += 1

print(num_squares)