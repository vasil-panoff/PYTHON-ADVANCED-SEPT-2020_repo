def even_odd(*args):
    command = args[-1]
    # or    x = 0 if args[-1] == "even" else 1
    #       return [num for num in args[:-1] if num % 2 == x]
    if command == "even":
        return [num for num in args[:-1] if num % 2 == 0]
    else:
        return [num for num in args[:-1] if num % 2 != 0]
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))