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

#Testcase 1
result=funList([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],10)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#calling function
#Testcase 2
result=funList([100,20,300,40,50,60,100],[100,20,300,40,50,60,100],20)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#calling function
#Testcase 3
result=funList([100,21,300,41,50,63,100],[100,21,300,41,50,63,100],10)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#calling function
#Testcase 4
result=funList([10,20,30,40,50],[10,20,30,40,50],10)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#calling function
#Testcase 5
result=funList([10,20,30,40,50],[100,150,200,250,300],5)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#calling function
#Testcase 6
result=funList([100,150,200,250,300],[100,150,200,250,300],10)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#calling function
#Testcase 7
result=funList([10,20,30,40,50],[1,2,3,4,5],5)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#calling function
#Testcase 8
result=funList([30,60,90,300,600],[30,60,90,300,600],30)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#calling function
#Testcase 9
result=funList([10,20,30,40,50],[1,2,3,4,5,6,7,8,9,10],4)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#calling function
#Testcase 10
result=funList([10,20,30,40,50],[100,150,200,250,300],100)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#