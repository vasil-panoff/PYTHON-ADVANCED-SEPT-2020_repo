from collections import deque

numbers = [int(x) for x in input().split(' ')]
to_enqueue, to_dequeue, searched_number = numbers

queue = deque([int(x) for x in input().split(' ')])

for _ in range(to_dequeue):
    queue.popleft()
if searched_number in queue:
    print("True")
else:
    if queue:
        print(min(queue))
    else:
        print(0)

print(list(queue))
