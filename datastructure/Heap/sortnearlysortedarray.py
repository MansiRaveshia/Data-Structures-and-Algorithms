#Sort a nearly sorted (or K sorted) array
# A Python3 program to sort a 
# nearly sorted array. 
import heapq
# Given an array of size n, where every   
# element is k away from its target  
# position, sorts the array in O(nLogk) time. 
def sort_k(arr, n, k): 
    # List of first k+1 items 
    h=arr[:k+1]
    # using heapify to convert list  
    # into heap(or min heap) 
    heapq.heapify(h)
    # "rem_elmnts_index" is index for remaining  
    # elements in arr and "target_index" is  
    # target index of for current minimum element  
    # in Min Heap "heap". 
    target_index=0
    for remaining in range(k+1,n):
        arr[target_index]=heapq.heappop(h)
        heapq.heappush(h,arr[remaining])
        target_index+=1
    while h:
        arr[target_index]=heapq.heappop(h)
        target_index+=1


# Driver Code 
k = 3
arr = [2, 6, 3, 12, 56, 8] 
n = len(arr) 
sort_k(arr, n, k) 
for elem in arr: 
    print(elem, end = ' ') 
