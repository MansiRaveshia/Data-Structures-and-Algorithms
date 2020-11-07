import heapq 
  #prg 1
# initializing list 
li = [5, 7, 9, 1, 3] 
  
# using heapify to convert list into heap 
heapq.heapify(li) 
  
# printing created heap 
print ("The created heap is : ",end="") 
print (list(li)) 
  
# using heappush() to push elements into heap 
# pushes 4 
heapq.heappush(li,4) 
  
# printing modified heap 
print ("The modified heap after push is : ",end="") 
print (list(li)) 
  
# using heappop() to pop smallest element 
print ("The popped and smallest element is : ",end="") 
print (heapq.heappop(li)) 


 #prg 2
print()
li1 = [5, 7, 9, 4, 3] 
  
# initializing list 2 
li2 = [5, 7, 9, 4, 3] 
  
# using heapify() to convert list into heap 
heapq.heapify(li1) 
heapq.heapify(li2) 
  
# using heappushpop() to push and pop items simultaneously 
# pops 2 
print ("The popped item using heappushpop() is : ",end="") 
print (heapq.heappushpop(li1, 2)) 
  
# using heapreplace() to push and pop items simultaneously 
# pops 3 
print ("The popped item using heapreplace() is : ",end="") 
print (heapq.heapreplace(li2, 2)) 