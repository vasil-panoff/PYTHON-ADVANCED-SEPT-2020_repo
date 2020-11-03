# text = input()
# idx = 0
# second_idx = -1
#
# while True:
#     if idx == len(text) // 2:
#         print(f"{text} is a palindrome")
#         break
#     if text[idx] == text[second_idx]:
#         idx += 1
#         second_idx -= 1
#     else:
#         print(f"{text} is not a palindrome")
#         break

def palindrome(text, idx):
    second_idx = len(text) - 1 - idx
    if idx == len(text) // 2:
        return f"{text} is a palindrome"
    if text[idx] == text[second_idx]:
        return palindrome(text, idx + 1)
    else:
        return f"{text} is not a palindrome"

print(palindrome("abcba", 0))