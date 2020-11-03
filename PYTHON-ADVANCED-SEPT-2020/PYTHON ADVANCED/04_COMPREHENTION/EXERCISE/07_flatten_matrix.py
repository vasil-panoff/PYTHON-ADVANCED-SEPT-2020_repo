line = input()
result = [el for x in line.split("|")[::-1] for el in x.split()]  # [::-1] is reversed slicing
print(" ".join(result))


