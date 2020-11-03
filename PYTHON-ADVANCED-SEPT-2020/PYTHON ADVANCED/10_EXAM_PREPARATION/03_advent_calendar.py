def fix_calendar(*args):
    numbers = args
    for i in args:
        num_one = i[0]
        num_two = i[1]
        num_three = i[2]

        num_one_is_bigest = False
        num_two_is_bigest = False
        num_three_is_biest = False

        if num_one > num_two and num_two > num_three:
            num_one_is_bigest = True
        elif num_one < num_two and num_two > num_three:
            num_two_is_bigest = True
        else:
            num_three_is_biest = True

    numbers = [num_one_is_bigest, num_two_is_bigest, num_three_is_biest]

    return fix_calendar(numbers)


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)