'''4. Write a function to take 2 lists and an integer X.
      Use zip function to iterate the list and pick values that
      are common at both indexes, they must be divisible by X. 
   *** Note: You must iterate the lists only if the lengths of the lists are equal***.
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
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
    :param orgList: Original listA passed by the User
    :param orgList: Original listB passed by the User
    :param numX: Number X passed by the User. Type is INT
    :return: New list with filtered values ONLY.

Solution Steps:
1. Take two lists and iterate both list using zip
2. From the list pick the comman elelments in both lists
3. To check the condition filter values are divisilble 
4. Return the list  
'''

# this function define for which indexes are same in both lists and it must divisible by numx
def funList(orgListA,orgListB,numX):
    # define empty list
    new_List = []
    # this will condition is will demonstrate both lists are equal
    orgListA = orgListB
    #  Iterate the original lists and filter the values
    for i,j in zip(orgListA,orgListB):
        # it will print the iteration elemants of the both lists
        print(i,j)
        # checking the condition the list elements are divisible or not if condition is truei
        # it will  executes if statment
        if (i%numX==0):
             # new elements add to the newlist
            new_List.append(i)
    # finally return new list      
    return new_List
# Execution
testListA=[100,20,300,40,50,60,100]
testListB=[1100,20,1300,40,50,160,1000]
numX=10
result=funList(orgListA=testListA,orgListB=testListB,numX=numX)
print("Final Result is :: {} ".format(result))

# Example2:
# Execution
testListA=[100,20,300,40,50,60,100]
testListB=[100,20,300,40,50,60,100]
numX=20
result=funList(orgListA=testListA,orgListB=testListB,numX=numX)
print("Final Result is :: {} ".format(result))

# Example3:
# Execution
testListA=[100,21,300,41,50,63,100]
testListB=[100,21,300,41,50,63,100]
numX=10
result=funList(orgListA=testListA,orgListB=testListB,numX=numX)
print("Final Result is :: {} ".format(result))