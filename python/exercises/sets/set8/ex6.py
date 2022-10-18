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
def funList(orglistA,orglistB,orglistC,numX,numY):
    #define new list
    new_List=[]
    #iterate three lists simantanously
    for i,j,k in zip(orglistA,orglistB,orglistC):
        #checking condition for sum of same indexes numbers in three lists is greater than sum of number x and number y
        if((i+j+k)>(numX+numY)):
            #adding numbers as list into new list
            new_List.append([i,j,k])
    #fiinally return new list        
    return new_List    
#calling function
#Testcase 1
result=funList([10,20,30,40,50],[1,2,3,4,5],[100,150,200,250,300],150,100)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList([10,20,30,40,50],[1,2,3,4,5],[100,150,200,250,300],50,100)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList([10,20,30,40,50],[1,2,3,4,5],[100,150,200,250,300],500,100)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ---------------------------------------------------------------------#
#Testcase 4
result=funList([10,20,30,40,50],[1,2,3,4,5],[100,150,200,250,300],5,10)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ---------------------------------------------------------------------#
#Testcase 5
result=funList([10,20,30,40,50,100,200],[1,2,3,4,5],[100,150,200,250,300],20,30)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ---------------------------------------------------------------------#
#Testcase 6
result=funList([10,20,30,40,50],[1,2,3,4,5,6,7,7],[100,150,200,250,300],50,10)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ---------------------------------------------------------------------#
#Testcase 7
result=funList([10,20,30,40,50],[1,2,3,4,5],[100,150,200,250,300,350,450],200,100)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ---------------------------------------------------------------------#
#Testcase 8
result=funList([10,20,30,40,50,100,200],[1,2,3,4,5],[100,150,200,250,300],300,200)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ---------------------------------------------------------------------#
#Testcase 9
result=funList([10,20,30,40,50,150,250],[1,2,3,4,5],[100,150,200,250,300],40,30)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ---------------------------------------------------------------------#
#Testcase 10
result=funList([10,20,30,40,50],[1,2,3,4,5,6,7,8,9,10],[100,150,200,250,300],7,8)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ---------------------------------------------------------------------#
