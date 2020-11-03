from functools import reduce

def operate(op, *args):
    if op == '+':
        return reduce(lambda a, b: a + b, args)
    if op == '-':
        return reduce(lambda a, b: a - b, args)
    if op == '/':
        return reduce(lambda a, b: a / b, args)
    if op == '*':
        return reduce(lambda a, b: a * b, args)

# or

def operate(op, *args):
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    return reduce(ops[op], args)

print(operate('-', *[i for i in range(1, 10)]))