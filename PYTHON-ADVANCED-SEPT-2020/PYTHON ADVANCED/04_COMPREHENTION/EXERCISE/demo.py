def generate_col():
    return [j
            for j in range(5 + 1)]

matrix = [generate_col()
          for i in range(5 + 1)]
print(matrix)

flattend_matrix = [col
                   for row in matrix
                   for col in row]
print(flattend_matrix)

