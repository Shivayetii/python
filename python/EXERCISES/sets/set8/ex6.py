'''
6. Write a function to take 3 lists, numX, numY as arguments.
    If the sum of elements in the indexes is > er sum of numX + numY, then add to new list.
    Finally return the new list.
    Note: You must execute only if the lists are of same length.
    Example 1  :
        listA=[10,20,30,40,50]
        listB=[1,2,3,4,5]
        listC=[100,150,200,250,300]
        numX=150
        numY=100
        result=func_exec(listA)
        print(result)
        Expected Output : [[40,4,250],[50,5,300]]
        Reason: 
            sum of (numX + numY) = 250
            -    sum of ([40,4,250]) is > er than sum of (numX + numY)
            -    sum of ([50,5,300]) is > er than sum of (numX + numY)
    Example 2 :
        listA=[10,20,30,40,50]
        listB=[1,2,3,4,5]
        listC=[100,150,200,250,300]
        numX=50
        numY=100
        result=func_exec(listA)
        print(result)
        Expected Output : [[20,2,150], [30,3,200], [40,4,250],[50,5,300]]
        Reason:
            sum of (numX + numY) = 150 
            -    sum of ([20,2,150]) is > er than sum of (numX + numY)
            -    sum of ([30,3,200]) is > er than sum of (numX + numY)                        
            -    sum of ([40,4,250]) is > er than sum of (numX + numY)
            -    sum of ([50,5,300]) is > er than sum of (numX + numY)
    Example 3  :
        listA=[10,20,30,40,50]
        listB=[1,2,3,4,5]
        listC=[100,150,200,250,300]
        numX=500
        numY=100
        result=func_exec(listA)
        print(result)
        Expected Output : []
        Reason: 
           sum of (numX + numY) = 600
           Sum of values in the indexes are < 600
        :param org_lists: Original lists (Org_listA,Org_listB,Org_listC)passed by the User
        :param numx: Numberx passed by the User. Type is INT.
        :param numy: Numbery passed by the User. Type is INT.
        :param numz: Numberz passed by the User. Type is INT.
        :return: New list with filtered values ONLY.    
           
    Solution Steps:
    **************
    Take three list and iterate simantanously
        checking sum of numbers in same indexes of three list is greater sum of number X and number Y  
        if Yes:
            add numbers as list to new list
        else:
            continue loop
    finally return new list             
'''
#define function
def funList(orgListA,orgListB,orgListC,numX,numY):
    #define new list
    new_list=[]
    #iterate three lists simantanously
    for i,j,k in zip(orgListA,orgListB,orgListC):
        #checking condition for sum of same indexes numbers in three lists is greater than sum of number x and number y
        if((i+j+k)>(numX+numY)):
            #adding numbers as list into new list
            new_list.append([i,j,k])
    #fiinally return new list        
    return new_list 
# Execution
# Example1
testListA=[10,20,30,40,50]
testListB=[1,2,3,4,5]
testListC=[100,150,200,250,300]
numX=150
numY=100
result=funList(orgListA=testListA,orgListB=testListB,orgListC=testListC,numX=numX,numY=numY)
print("Final Result is :: {} ".format(result))
# Example2
testListA=[10,20,30,40,50]
testListB=[1,2,3,4,5]
testListC=[100,150,200,250,300]
numX=00
numY=100
result=funList(orgListA=testListA,orgListB=testListB,orgListC=testListC,numX=numX,numY=numY)
print("Final Result is :: {} ".format(result))
# Example3
testListA=[10,20,30,40,50]
testListB=[1,2,3,4,5]
testListC=[100,150,200,250,300]
numX=500
numY=100
result=funList(orgListA=testListA,orgListB=testListB,orgListC=testListC,numX=numX,numY=numY)
print("Final Result is :: {} ".format(result))