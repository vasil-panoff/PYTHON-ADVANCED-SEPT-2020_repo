rows, cols = [int(element) for element in input().split(', ')]
matrix = []
total = 0

for _ in range(rows):
    row = [int(number) for number in input().split(', ')]
    assert len(row) == cols, f'Expecting {cols} columns, got {len(row)}'
    matrix.append(row)
    total += sum(row)

print(total)
print(matrix)

# import itertools
#
# rows, cols = [int(element) for element in input().split(', ')]
# matrix = [[int(number) for number in input().split(', ')] for _ in range(rows)]
# total = sum(itertools.chain(*matrix))
#
# print(total)
# print(matrix)
