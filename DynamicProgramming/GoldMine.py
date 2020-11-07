# Python program to solve 
# Gold Mine problem
  
# Returns maximum amount of 
# gold that can be collected 
# when journey started from 
# first column and moves 
# allowed are right, right-up 
# and right-down 
def getMaxGold(gold, m, n): 
  
    # Create a table for storing 
    # intermediate results 
    # and initialize all cells to 0. 
    # The first row of 
    # goldMineTable gives the 
    # maximum gold that the miner 
    # can collect when starts that row 
    goldtable=[[0 for j in range(n)] for i in range(m)]
    for col in range(n-1,-1,-1):
        for row in range(m):
            if (row==0 or col==n-1):
                right_up=0
            else:
                right_up=goldtable[row-1][col+1]
            if col==n-1:
                right=0
            else:
                right=goldtable[row][col+1]
            if (row==m-1 or col==n-1):
                right_down=0
            else:
                right_down=goldtable[row+1][col+1]
            goldtable[row][col]=gold[row][col]+max(right,right_down,right_up)

    res=goldtable[0][0]
    for i in range(m):
        res=max(res,goldtable[i][0])

    return res


gold = [[1, 3, 1, 5], 
    [2, 2, 4, 1], 
    [5, 0, 2, 3], 
    [0, 6, 1, 2]] 
  
m = 4
n = 4
  
print(getMaxGold(gold, m, n)) 
  