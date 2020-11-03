command = input()

while True:
    numbers = list(map(int, input().split(' ')))
    if command == "Even":
        even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
        print(sum(even_numbers) * len(numbers))
    elif command == "Odd":
        odd_numbers = list(filter(lambda number: number % 2 == 1, numbers))
        print(sum(odd_numbers) * len(numbers))
    break