def print_matrix(matrix):
    for i in range(M):
        print(' '.join(matrix[i]))

def is_valid(matrix, cmd):
    if cmd and cmd[0] != 'swap':
        return False
    if len(cmd[1:]) != 4:
        return False
    i1, j1, i2, j2 = tuple(map(int, cmd[1:]))

    if i1 < 0 or i1 >= M:
        return False
    if i2 < 0 or i2 >= M:
        return False
    if j1 < 0 or j1 >= N:
        return False
    if j2 < 0 or j2 >= N:
        return False

    return True

M, N = tuple(map(int, input().split(' ')))

matrix = [[0] * N for i in range(M)]

for i in range(M):
    row = input().split(' ')

    for j in range(N):
        matrix[i][j] = row[j]


cmd = input()
while cmd != 'END':
    cmd = cmd.split(' ')
    if is_valid(matrix, cmd):
        i1, j1, i2, j2 = tuple(map(int, cmd[1:]))
        tmp = matrix[i1][j1]
        matrix[i1][j1] = matrix[i2][j2]
        matrix[i2][j2] = tmp

        print_matrix(matrix)
    else:
        print('Invalid input!')

    cmd = input()

