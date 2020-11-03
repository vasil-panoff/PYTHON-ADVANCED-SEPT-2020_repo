def operate(operator, *nums):
    return eval(''.join(map(lambda n: f'{operator}{n}', nums))[1:])