GROWING: int = 1  # global namespace
SHRINKING: int = -1


def print_rhombus(n: int):  # global namespace

    # fn-in-fn: closure
    def print_line(i: int, direction: int):  # locale namespace: visible in print_rhombus
        if i == 0:
            return
        line = ' ' * (n - i) + '* ' * i
        print(line.rstrip())
        if i == n:
            direction = SHRINKING # chainge is happening in local namespace
        print_line(i + direction, direction) # recurcion
    print_line(1, GROWING)

print_rhombus(int(input()))