possible_moves = (
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1),
    (-2, 1),
    (-2, -1),
)

board_size = int(input())

matrix = [['0'] * board_size for i in range(board_size)]


def is_valid(i, j):
    if i < 0 or j < 0 or i >= board_size or j >= board_size:
        return False

    return matrix[i][j] == "K"

knights_dict = {}

def update_knights(i1, j1, i2, j2):
    if not is_valid(i2, j2):
        return

    if (i2, j2) not in knights_dict:
        knights_dict[(i2, j2)] = []
    knights_dict[(i2, j2)].append((i1, j1))

    if (i1, j1) not in knights_dict:
        knights_dict[i1, j1] = []
    knights_dict[(i1, j1)].append((i2, j2))


for i in range(board_size):
    row = list(input())

    for j in range(board_size):
        if row[j] == "K":
            matrix[i][j] = "K"

            for move_i, move_j in possible_moves:
                i1 = i
                j1 = j
                i2 = i + move_i
                j2 = j + move_j


                update_knights(i1, j1, i2, j2)

num_removed = 0
max_knight = get_max_knight(knights_dict)
while len(max_knight) > 0:
    remove_knight(matrix, max_knight)
    knights_dict

    num_removed += 1

print(num_removed)
