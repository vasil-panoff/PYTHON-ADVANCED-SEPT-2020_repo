def baba(a, *args, **kwargs):
    print(args)
    print(kwargs)

baba(1, 1, test=5)


###########################

from functools import reduce

def add(a, b):
    print(f'a = {a}')
    print(f'b = {b}')
    return a + b
res = reduce(add, [1,2,3,4])
print(f'res = {res}')

##############################

from operator import mul

def multiply(*args):
    return reduce(mul, args)

###############################

import math

multiply = lambda *args: math.prod(args)
print(multiply(1,2))

##############################

def baba(*args, **kwargs):
    print(args)
    print(kwargs)

baba(*[1, 2, 3], **{"a": 1, "b": 2})

