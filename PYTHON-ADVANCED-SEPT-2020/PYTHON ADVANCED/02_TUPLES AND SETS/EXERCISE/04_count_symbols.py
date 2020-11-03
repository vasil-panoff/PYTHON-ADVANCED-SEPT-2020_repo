phrase = tuple(input())

unique_chars = set(phrase)

for char in sorted(unique_chars):
    print(f'{char}: {phrase.count(char)} time/s')
