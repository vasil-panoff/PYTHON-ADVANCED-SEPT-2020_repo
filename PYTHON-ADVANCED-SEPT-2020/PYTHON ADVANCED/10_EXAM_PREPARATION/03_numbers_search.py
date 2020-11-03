def numbers_searching(*args):
    result = [
        n
        for n in args
    ]
    unique = sorted(list(set([x for x in result if result.count(x)])))
    start_number = unique[0]
    end_number = unique[-1]

    missing_numbers = [i for i in range(start_number, end_number) if i not in unique]
    first_missing_not_in_my_list = missing_numbers[0]

    return [first_missing_not_in_my_list, unique]

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))