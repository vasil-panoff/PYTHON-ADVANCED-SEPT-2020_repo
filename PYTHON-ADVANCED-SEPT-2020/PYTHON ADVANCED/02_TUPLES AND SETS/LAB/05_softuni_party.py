n = int(input())
quests = set()
attended = set()

for _ in range(n):
    num = input()
    quests.add(num)

while True:
    command = input()
    if command == "END":
        break
    attended.add(command)

unattended = quests - attended
print(len(unattended))
print("\n".join(sorted(unattended)))