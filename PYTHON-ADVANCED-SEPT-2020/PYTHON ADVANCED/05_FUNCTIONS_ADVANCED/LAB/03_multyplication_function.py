from functools import reduce

multiply = lambda *args: reduce(lambda a, b: a * b, args)
print(multiply(1, 2, 3, 4, 5))

# or

def multiply (*args):
    return reduce(lambda a, b: a * b, args)
print(multiply(1, 2, 3, 4, 5))

# or

def multiply(*args):
    result = 1
    for num in args:
        result *= num
        return result
