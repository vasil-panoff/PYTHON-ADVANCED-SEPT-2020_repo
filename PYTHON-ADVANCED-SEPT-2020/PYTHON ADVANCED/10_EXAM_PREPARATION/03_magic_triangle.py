def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for row in range(2, n):
        new_row = []
        for col in range(0, row + 1):
            if col - 1 < 0:
                new_row.append(1)
            elif col >= len(triangle[row-1]):
                new_row.append(1)
            else:
                upper_left = triangle[row - 1][col - 1]
                upper_right = triangle[row - 1][col]
                new_value = upper_left + upper_right
                new_row.append(new_value)
        triangle.append(new_row)

    return triangle

print(get_magic_triangle(3))

