# Python3 program to print a fraction  
# in Egyptian Form using Greedy 
# Algorithm 
#taken from geeks for geeks
# import math package to use 
# ceiling function 
import math 
  
# define a function egyptianFraction  
# which receive parameter nr as 
# numerator and dr as denominator 
def egyptianFraction(nr, dr): 
    print("egyptian fraction representation of {0}/{1} is".format(nr,dr),end="\n")
    l=[]
    while nr!=0:
        x=math.ceil(dr/nr)
        l.append(x)
        nr=nr*x-dr
        dr=x*dr
    for x in range(len(l)):
        if x!=len(l)-1:
            print("1/{0} + ".format(l[x]),end="")
        else:
            print("1/{0} ".format(l[x]),end="")


egyptianFraction(6, 14) 
