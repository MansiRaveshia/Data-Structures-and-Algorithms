# Program to find the maximum profit  
# job sequence from a given array 
# of jobs with deadlines and profits 
  
# function to schedule the jobs take 2  
# arguments array and no of jobs to schedule 
def printJobScheduling(arr, t): 
  
    # length of array 
    n = len(arr) 
    arr.sort(key=lambda x : x[2],reverse=True)
    # To keep track of free time slots 
    # To store result (Sequence of jobs) 
    job = [-1 for x in range(t)]
    print(job) 

  
    # Iterate through all given jobs 
    for i in range(len(arr)): 
  
        # Find a free slot for this job  
        # (Note that we start from the  
        # last possible slot) 
        #slots are from 0 to 2 i.e 3 slots
        for j in range(arr[i][1]-1, -1, -1): 
              
            # Free slot found 
            if job[j]==(-1):
                job[j] = arr[i][0] 
                break
  
    # print the sequence 
    print(job) 


arr = [['a', 2, 100], # Job Array 
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]] 
t=max(x[1] for x in arr)
  
print("Following is maximum profit sequence of jobs") 
printJobScheduling(arr, t)