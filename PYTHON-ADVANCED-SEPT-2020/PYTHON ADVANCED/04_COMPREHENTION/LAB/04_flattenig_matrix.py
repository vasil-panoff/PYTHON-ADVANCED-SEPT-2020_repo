print([int(n) for _ in range(int(input())) for n in input().split(', ')])

# or

l = []
for _ in range(int(input())):
    for n in input().split(', '):
        l.append(int(n))
print(l)