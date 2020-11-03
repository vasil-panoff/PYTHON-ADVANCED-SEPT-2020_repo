def operate(operator=None, *args):
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else a / 1
    }

    if len(args) == 0:
        return 0
    elif len(args) == 1:
        return args[0]
    else:
        num1, num2, *rest = args
        result = operations[operator](num1, num2)
        return operate(operator, result, *rest)