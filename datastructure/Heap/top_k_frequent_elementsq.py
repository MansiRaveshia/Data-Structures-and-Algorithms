#find top k elements with highest frequency
import heapq
def topk(a,k):
    freq = {}
    freq_list=[]  
    for n in a:
        if n in freq:
            freq[n]=freq[n]+1
        else:
            freq[n]=1
    for key in freq.keys():
        freq_list.append((freq[key],key))
    heapq._heapify_max(freq_list)
    topk=[]
    for i in range(k):
        topk.append(heapq._heappop_max(freq_list))
    return topk

arr = [7, 10, 11, 5, 2, 5, 5, 7, 5, 11, 10, 11, 8, 9]
print(topk(arr,3))



 