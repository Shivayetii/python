'''2. Write a function to take a list, number Y as arguments.
    Filter all the numbers from the EVEN indexes, divisible by number Y. Remove duplicates.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        numY=10
        result=func_exec(listA,numY)
        print(result)
        Expected Output : [30,50,100]
    Example :
        listA=[10,21,301,41,501,50,1100,11,12,13]
        numY=10
        result=func_exec(listA,numY)
        print(result)
        Expected Output : [1100]
    Example :
        listA=[10,20,30,40,50,60,100,11,120,13,100]
        numY=10
        result=func_exec(listA,numY)
        print(result)
        Expected Output : [30,50,100,120]
    :param listA: List passed by the User
    :param::param numX: Number X passed by the User. Type is INT.
    :return: Filter the all even numbers indexes and divisible those indexes by numY and return new list
    
Solution Steps :
----------------
1. From the list, filter all elements from the Even index
2 . After filter even indexes divisible by numY
3. Remove duplicates from Even List
4. Return new list
'''
# This function will define filter all even indexes in list and which elements are divisible by numY
def funList(orgList,numY):
    # define empty list
    new_List = []
    # Iterate the original list
    for i in range(2,len(orgList),2):
        # this condition is check for which even elements divisible by numY it condition is true
        # it will executes if statment
        if (orgList[i]%numY==0):
          # it will remove the duplicate elements in new list
          if (i not in new_List):
            # add new elements in the list
            new_List.append(orgList[i])
    # finally return new list
    return new_List
#calling function
#Testcase 1
result=funList([10,20,30,40,50,60,100,11,12,13],10)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList([10,21,301,41,501,50,1100,11,12,13],10)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList([10,20,30,40,50,60,100,11,120,13,100],10)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList([10,20,30,40,50,60,100,11,12,13,13,14,13],5)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funList([10,20,30,40,50,60,100,11,12,13,50,14,50],8)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funList([10,20,30,40,50,60,100,11,12,13,111,122,100,101,100],20)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funList([10,20,30,40,50,60,100,11,12,13,40,30,40,1,40],6)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funList([10,20,30,40,50,60,100,11,12,13,20,1,20],9)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funList([10,20,30,40,50,60,100,11,12,13,30,3,30],4)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funList([10,20,30,40,50,60,100,11,12,13,10,10],3)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#