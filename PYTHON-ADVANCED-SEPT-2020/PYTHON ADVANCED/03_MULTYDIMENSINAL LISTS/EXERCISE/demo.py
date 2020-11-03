# list = [1, 2, 3]
#
# multydimentional_list = [
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3],
# ]

M = 2
N = 3

# matrix = []
#
# for i in range(M):
#     matrix.append([])
#
#     for j in range(N):
#         matrix[i].append(0)

matrix = [[0] * N for i in range(M)]

print(matrix)