import heapq
def maxheapsort(iterables):
    h=[]
    for data in iterables:
        heapq.heappush(h,-data)
    return [-heapq.heappop(h) for x in range(len(h))]

def maxheapsort2(iterables):
    h=[]
    for data in iterables:
        heapq.heappush(h,data)
    heapq._heapify_max(h)
    return [heapq._heappop_max(h) for x in range(len(h))]


def minheapsort(iterables):
    h=[]
    for data in iterables:
        heapq.heappush(h,data)
    return [heapq.heappop(h) for x in range(len(h))]

print(maxheapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
print(maxheapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
print(minheapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
