import heapq

'''
T1 = 5
T2 = 4
T3 = 7
T4 = 9
T5 - 2
T6 - 6
'''

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
data2 = [15, 20, 25, 30]
data3 = heapq.merge(data, data2)
print("Merged -", list(data3))
# data = [-x for x in data]  # for min heap

heapq.heapify(data)
print(data)

print(heapq.heappop(data))
print(data)

heapq.heappush(data, 34)
heapq.heappush(data, 100)
heapq.heappush(data, 4)

print(data)