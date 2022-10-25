''' Write a function to take 2 lists and an integer numX.
   Use zip function to iterate the list.
   Pick values if 
           :they are common at both indexes AND 
           :they ARE be divisible by numX. 
   
   Duration for Dev & Execution: 10 minutes
   -----------------------------------------
   
   *** Note: You must iterate the lists only if the lengths of the lists are equal. *** 
   -------------------------------------------------------------------------------------
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,260,1000]0,1300,40,50,1
        numX=10
        result=func_exec(listA,listB)
        print(result)
        Expected Output : []
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[100,20,300,40,50,60,100]
        numX=20
        result=func_exec(listA,listB)
        print(result)
        Expected Output : [100,20,300,40,50,60,100]
    Example :
        listA=[100,21,300,41,50,63,100]
        listB=[100,21,300,41,50,63,100]
        numX=10
        result=func_exec(listA,listB)
        print(result)
        Expected Output : [100,300,50,100]
'''
def funList(orgListA,orgListB,numX):
    newList = []
    for i,j in zip(orgListA,orgListB):
        if(i==j):
            if(i%numX==0):
                newList.append(i)
    return newList
#print(funList([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],10))
print(funList([100,20,300,40,50,60,100],[100,20,300,40,50,60,100],20))