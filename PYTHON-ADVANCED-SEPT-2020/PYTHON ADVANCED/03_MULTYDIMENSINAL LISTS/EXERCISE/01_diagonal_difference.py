N = int(input())

matrix = [[0] * N for i in range(N)]

sum_primary_diagonal = 0
sum_secondary_diagonal = 0

for i in range(N):
    row = list(map(int, input().split(' ')))

    for j in range (N):
        matrix[i][j] = row[j]

        if i == j:
            sum_primary_diagonal += matrix[i][j]

        if N - 1 - i == j:
            sum_secondary_diagonal += matrix[i][j]

print(abs(sum_primary_diagonal - sum_secondary_diagonal))
#    0M 1M 2M
# N0  1  2  3
# N1  4  5  6
# N2  7  8  9