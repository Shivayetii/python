'''3. Write a function to take a list, number X,Y,Z as arguments. 
      From the list pick the elements that are >er than (X+Y+Z). 
      Add those elements to new list. Finally return the new list.
    Example : 
        listA=[1,2,300,4,5,6,7,8,9,100,11,120,200,400]
        numX=10
        numy=20
        numZ=25
        result=func_exec(listA,numX,numY,numZ)
        print(result)
        Expected Output : [300,100,120,200,400]
        :param orgList: Original list passed by the User
        :param numX: Number X passed by the User. Type is INT.
        :param numY: Number X passed by the User. Type is INT.
        :param numZ: Number X passed by the User. Type is INT.
        :return: New list with filtered values ONLY.
        Example : 
        listA=[1,2,300,4,5,6,7,8,9,100,11,120,200,400]
        numX=10
        numy=20
        numZ=25
        result=func_exec(listA,numX,numY,numZ)
        print(result)
        Expected Output : [300,100,120,200,400]
solution steps:
1. Itertate original list = [1,2,300,4,5,6,7,8,9,100,11,120,200,400]
2. from the list filter which elements are greater than sum of numX,numY and numz
3. finally return new list
'''
#Tthis function define From the list pick the elements that are >er than (X+Y+Z)
def funList(orgList,numX,numY,numZ):
    #define an empty new list
    new_list=[]
    # total sum of three arguments numX,numY and numZ
    totSum = numX + numY+ numZ
    # itarate the list
    for i in orgList:
        # checking condition list of the elements greterthen sum of numx+numy+numz
        if (i>totSum):
            # #elements add to new list    
            new_list.append(i) 
    # finally returns a new list
    return new_list 
# Execution
testList=[1,2,300,4,5,6,7,8,9,100,11,120,200,400]
numX=10
numY=20
numZ=25
result=funList(orgList=testList,numX=numX,numY=numY,numZ=numZ)
print("Final Result is :: {} ".format(result))
