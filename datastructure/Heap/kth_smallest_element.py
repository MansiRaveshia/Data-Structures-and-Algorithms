#using max heap for this
import heapq
def small(a,k):
    h=[]
    heapq._heapify_max(h)
    for data in a:
        if len(h)<=k:
            heapq.heappush(h,data)
            heapq._heapify_max(h)
            
        if len(h)>k:
            heapq._heappop_max(h)
            heapq._heapify_max(h)
    return heapq.heappop(h)


a=[13,7,10,4,25,3,20,15]
print(small(a,3))