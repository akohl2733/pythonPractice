names = ["andrew", "abby", "chloe", 'zeke']
final = []

for i in range(len(names) - 1, -1, -1):
    final.append(names[i])

print(final)

for item in reversed(names):
    # print(item)
    pass


names2 = ['ronald', 'sandra', 'marie', 'charles']

names.extend(names2)
print("Extended names:", names)


from collections import deque

queue = deque(['watt', 'heyward', 'sutton', 'ramsey'])
queue.append('warren')
queue.append('johnson')
first_name_popped = queue.popleft()

print(queue, " - First name popped - ", first_name_popped)

final = [(x, y) for x in [1, 2, 3] for y in [3, 5, 6] if x!=y]
print("List Comprehension", final)