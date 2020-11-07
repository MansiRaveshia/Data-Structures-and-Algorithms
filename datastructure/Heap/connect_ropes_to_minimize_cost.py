import heapq
def ropes(h):
    heapq.heapify(h)
    sum=0
    while len(h)>1:
        x=heapq.heappop(h)
        y=heapq.heappop(h)
        z=x+y
        sum+=z
        heapq.heappush(h,z)
    
    return sum


a=[4, 3, 2 ,6]
print(ropes(a))