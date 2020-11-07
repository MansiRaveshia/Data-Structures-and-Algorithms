#find k closest points to origin
import math
import heapq
def korigin(a,k):
    l=[]
    for x,y in a:
        m=x*x+y*y
        n=x,y
        z=m,n
        l.append(z)
    heapq.heapify(l)
    topclosest=[]
    for i in range(k):
        topclosest.append(heapq.heappop(l)[-1])
    return topclosest

points = [[3, 3], [5, -1], [-2, 4],[0,0],[5,9]] 
k = 3
print(korigin(points,k))