def find_strongest_eggs(test, *args):
    sequence = test
    list_one = sequence[::2] # returns even positions of list
    list_two = sequence[1::2] # returns odd positions of list
    new_list = [list_one, list_two]
    max_number_list_one = max(list_one)
    max_number_list_two = max(list_two)
    final_list = [max_number_list_one, max_number_list_two]

    return final_list

test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))
