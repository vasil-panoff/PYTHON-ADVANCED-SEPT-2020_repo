# 1 2 -3 -4 65 -98 12 57 -84
numbers = list(map(lambda n: int(n), input().split(' ')))
# numbers_copy = numbers.copy()
# or   numbers = map(int, input().split(' '))
negatives = filter(lambda number: number < 0, numbers)
positives = filter(lambda number: number > 0, numbers)

sum_negatives = sum(negatives)
sum_positives = sum(positives)

print(sum_negatives)
print(sum_positives)

if abs(sum_negatives) > sum_positives:
    print("The negatives are stronger than the positives")
elif sum_positives > abs(sum_negatives):
    print("The positives are stronger than the negatives")
