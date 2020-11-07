#Find k closest numbers to a given no in an unsorted array
import heapq
import math
def kclosest(a,x,k):
    h=[]
    heapq.heapify(h)
    for element in a:
        heapq.heappush(h,(abs(element-x),element))
    heapq.heapify(h)
    print(heapq.nsmallest(k,h)[-1])


arr = [-10,-50,20,17,80] 
x,k = 20,2
kclosest(arr, x, k) 

