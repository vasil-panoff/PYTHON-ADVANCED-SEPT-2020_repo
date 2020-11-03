n, m = tuple([int(x) for x in input().split(' ')])

set_n = set()
set_m = set()

for i in range(n):
    set_n.add(input())

for i in range(m):
    set_m.add(input())

set_interesection = set_n & set_m

for elem in set_interesection:
    print(elem)
