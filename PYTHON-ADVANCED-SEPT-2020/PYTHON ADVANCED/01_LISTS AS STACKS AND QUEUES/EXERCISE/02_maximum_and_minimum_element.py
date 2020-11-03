# n = int(input())
#
# numbers = []
#
# for _ in range(n):
#     numbers = input().split()
#     command = int(numbers[0])
#     if command == 1:
#         numbers.append(int(numbers[1]))
#     elif command == 2:
#         if numbers:
#             numbers.pop()
#     elif command == 3:
#         if numbers:
#             print(max(numbers))
#     elif command == 4:
#         if numbers:
#             print(min(numbers))
#
# print(', '.join([str(x) for x in reversed(numbers)]))

# or

n  = int(input())
stack = []

for _ in range(n):
    numbers = [int(x) for x in input().split()]
    if numbers[0] == 1:
        stack.append(numbers[1])
    if stack:
        if numbers[0] == 2:
            stack.pop()
        elif numbers[0] == 3:
            print(max(stack))
        elif numbers[0] == 4:
            print(min(stack))

print(', '.join([str(x) for x in reversed(stack)]))