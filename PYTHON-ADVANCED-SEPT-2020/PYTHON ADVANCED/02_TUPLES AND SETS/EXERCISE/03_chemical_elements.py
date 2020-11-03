lines = int(input())

unique_elements = set()

for i in range(lines):
    line_set = set(input().split(' '))
    unique_elements = unique_elements | line_set

print("\n".join(unique_elements))

