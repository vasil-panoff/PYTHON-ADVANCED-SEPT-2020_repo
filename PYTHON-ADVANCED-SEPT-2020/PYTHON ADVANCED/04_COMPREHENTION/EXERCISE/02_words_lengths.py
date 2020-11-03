elements = input().split(', ')
result = [f"{x} -> {len(x)}" for x in elements]
print(", ".join(result))

# or with dictionary

elements = {x: len(x) for x in input().split(', ')}
result = [f"{key} -> {value}" for key, value in elements.items()]
print(", ".join(result))

