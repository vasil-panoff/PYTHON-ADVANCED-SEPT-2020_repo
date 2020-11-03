text_line = input().split(" ")
word_filter = [word for word in text_line if len(word) %2 == 0]
print ('\n'.join(word_filter))

# or

text_line = input().split(" ")
[print(word) for word in text_line if len(word) %2 == 0]