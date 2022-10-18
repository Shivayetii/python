'''
1. Write a function to take a list, numX, numY as arguments.
Filter all the numbers from the list that are >numX and <numY and add to new list.
Finally return the new list.
    Example 1 :
        listA=[10,20,30,40,50,60,100,11,12,13]
        numX=45
        numY=55
        result=func_exec(listA)
        print(result)
        Expected Output : [50]
        Reason: 50 is >er than numX 45 and <er than numY 55
    Example 2 :
        listA=[10,20,30,46,52,60,54,11,12,13]
        numX=45
        numY=55
        result=func_exec(listA)
        print(result)
        Expected Output : [46,52,54]
        Reason: 46 is >er than numX 45 and <er than numY 55
        Reason: 52 is >er than numX 45 and <er than numY 55
        Reason: 54 is >er than numX 45 and <er than numY 55
    Example 3 :
        listA=[10,20,30,46,52,60,54,11,12,13]
        numX=450
        numY=550
        result=func_exec(listA)
        print(result)
        Expected Output : []
        :param org_list: Original list passed by the User
        :param numx: Numberx passed by the User. Type is INT.
        :param numy: Numbery passed by the User. Type is INT.
        :return: New list with filtered values ONLY.  
    Solution Steps:
    **************
    Take a original list and iterate original list     
    Check if number is greater than number X and number less than number Y
        if yes:
            add to new list
        else:
            continue loop  
    Finally return new list              
'''
#define function
def funList(org_List,numX,numY):
    #define new list
    new_List=[]
    #iterate elements from original list one by one
    for i in org_List:
        #checking for element is greater than x and less than y
        if(i>numX and i<numY):
            #adding element to new list
            new_List.append(i)
    #finally return new list
    return new_List
#calling function
#Testcase 1
result=funList([10,20,30,40,50,60,100],45,55)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList([10,20,30,46,52,60,54,11,12,13],45,55)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList([10,20,30,46,52,60,54,11,12,13],450,550)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList([10,20,30,46,52,60,54,11,12,13,500],450,550)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funList([10,20,30,46,52,60,54,11,12,13,50],30,400)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funList([10,20,30,46,52,60,54,11,12,13,500,450,350],50,40)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funList([10,20,30,46,52,60,54,500],10,40)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funList([10,20,30,46,52,60,54,11,12,13,500,150,250,230],20,30)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funList([10,20,30,46,52,60,54,11,12,13,500,40,70,60],10,20)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funList([10,20,30,46,52,60,54,11,12,13,500,160,170,180],7,8)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#