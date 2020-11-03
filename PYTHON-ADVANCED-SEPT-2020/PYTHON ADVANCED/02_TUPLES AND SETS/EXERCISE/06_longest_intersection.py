num_lines = int(input())

intersections = []

for i in range(num_lines):
    set_1_values, set_2_values = tuple(input().split('-'))

    set_1_start_value, set_1_end_value = tuple(map(int, set_1_values.split(',')))
    set_1 = set(range(set_1_start_value, set_1_end_value + 1))

    set_2_start_value, set_2_end_value = tuple(map(int, set_2_values.split(',')))
    set_2 = set(range(set_2_start_value, set_2_end_value + 1))

    set_intersection = set_1 & set_2
    intersections.append(set_intersection)

longest_set = set()

for set_intersection in intersections:
    set_size = len(set_intersection)

    if set_size > len(longest_set):
        longest_set = set_intersection

print(f"Longest intersection is {sorted(list(longest_set))} with length {len(longest_set)}")