# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    #i is root node & n is size of array or binary tree
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
    # See if left child of root exists and is 
    # greater than root 
    if l<n and arr[l]>arr[i]:
        largest=l
    
    # See if right child of root exists and is 
    # greater than root     
    if r<n and arr[r]>arr[largest]:
        largest=r

     # Change root, if needed    
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]   # swap 
        heapify(arr,n,largest)   # Heapify the root. 


def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for j in range(n//2-1,-1,-1):
        heapify(arr,n,j) #n is size of array or tree

    # One by one extract elements
    for j in range(n-1,0,-1):
        arr[j],arr[0]=arr[0],arr[j]
        heapify(arr,j,0)


arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print (arr[i],end=" ")
        
