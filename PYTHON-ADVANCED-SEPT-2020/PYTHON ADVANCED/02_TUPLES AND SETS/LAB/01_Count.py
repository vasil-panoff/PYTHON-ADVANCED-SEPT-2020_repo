nums = tuple(float(t) for t in input().split())
s = set()

for number in nums:
    if number not in s:
        s.add(number)
        print(f"{number} - {nums.count(number)} times")




# from collections import defaultdict
#
# d = {}
#
# d = defaultdict(int)
# numbers = map(float, input().split(' '))
#
# for number in numbers:
#     d[number] +=1
#
# for number, occurence_count in d.items():
#     print(f'{number} - {occurence_count} times')