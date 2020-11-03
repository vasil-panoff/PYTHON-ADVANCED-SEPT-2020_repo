from itertools import chain
from functools import lru_cache

def read_matrix():
    rows, cols = [int(n) for n in input().split(', ')]
    matrix = [
        [int(n) for n in input().split(', ')]
        for _ in range(rows)
    ]
    return matrix


def get_squares(matrix):
    squares = []
    for i in range(len(matrix) - 1):
        row = matrix[i]
        for j in range(len(row) - 1):
            square = [
                matrix[i][j:j+2],
                matrix[i + 1][j:j+2],
            ]
            squares.append(square)
    return squares

@lru_cache(maxsize=50)
def get_sum_of_martix(matrix):
    return sum(chain(*matrix))


def get_max_square(squares):


    max_square_sum = None
    max_square = None
    for square in squares:
        square_sum = get_sum_of_martix(square)
        if max_square_sum is None or square_sum > max_square_sum:
            max_square_sum = square_sum
            max_square = square
    return  max_square

matrix = read_matrix()
squares = get_squares(matrix)
max_square = get_max_square(squares)

print('\n'.join([' '.join(map(str, row)) for row in max_square]))
print(get_sum_of_martix(max_square))
