# n --> Total number of activities 
# s[]--> An array that contains start time of all activities 
# f[] --> An array that contains finish time of all activities 
def max_activity(s,f):
    n=len(s)
    activity=list(range(n))
    activity.sort(key=lambda i:f[i])
    #sorted activities number according to ascending order of finish time i.e f
    a=list(zip(s,f))
    a.sort(key=lambda x:x[1])
    # here x represents a tuple from list 
    #x[1] represents 2nd element of tuple i.e finish time i.e f 
    #in list, tuple of start and finish time are sorted based on finish time
    #sorted pairs of start & end time in ascending order of finish time
    l1,l2=zip(*a) #unpacking tuples of list 
    #l1=start time
    #l2=finish time in sorted order
    print(activity[0])
    i=0
    for j in range(1,n):
        if l1[j]>=l2[i]:
            print(activity[j])
            i=j
    

                                       
s=[5,1,3,0,5,8]
f=[9,2,4,6,7,9]      
max_activity(s,f)                                 



    
