#find n largest and n smallest elements from array
import heapq
heap = [23, 7, -4, 18, 23, 42, 37, 2, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(heap)
print(heapq.nlargest(3, heap))  # [42, 42, 37]
print(heapq.nsmallest(3, heap)) # [-4, -4, 2]

#prg to get kth largest from array
print()
nums= [3,2,1,5,6,4]
k = 2  #k being the kth largest element you want to get
heapq.heapify(nums) 
temp = heapq.nlargest(k, nums)
print(temp[-1])
#to get kth smallest
temp = heapq.nsmallest(k, nums)
print(temp[-1])
