num_users = int(input())

unique_users = set()

for _ in range(num_users):
    username = input()
    unique_users.add(username)

for username in unique_users:
    print(username)

