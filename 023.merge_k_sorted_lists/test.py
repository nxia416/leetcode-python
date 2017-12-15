import heapq
from solution import Solution


solution = Solution()
# solution.mergeKLists2([[1,3,4,6], [2,6,23,75,647]])


h = []
for value in [23,42,2,17, 89]:
    print(value)
    heapq.heappush(h, value)

print("==========")

l = heapq.heappop(h)
print(l)
l = heapq.heappop(h)
print(l)
l = heapq.heappop(h)
print(l)
l = heapq.heappop(h)
print(l)

print(h)
