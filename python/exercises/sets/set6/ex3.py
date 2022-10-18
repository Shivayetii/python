'''
3. Write a function to take a list. Select the number that is greater than product of all other numbers.
    Example :
        listA=[1,2,30,4,2]
        result=func_exec(listA)
        print(result)
        Expected Output : 30
        Reason: 30 is greater than product of [1,2,4,2] -> 16
    Example :
        listA=[1,2,3,4,2]
        result=func_exec(listA)
        print(result)
        Expected Output : []
        :param org_list: Original list passed by the User        
        :return: New list with filtered values ONLY
Solution Steps:
**************
Iiterate the original list
    Find the current number, store in a variable currNumber
        Find the product of remaining numbers and store in a variable sumList
        Check if currNumber is >er productList:
            If yes:
                return currNumber
            else:
                continue the LOOP  
Finally return the new list             
'''
# This function is define pick greater number sum of all the list       
def funList(org_list):
    # iterate the orginal list
    for i in org_list:
        # assigning org list to another variable like new_mapper 
        new_List=org_list
        # remove a selected element from the New list
        new_List.remove(i)
        # logic for product
        list_product=1
        for j in new_List:            
            list_product*=j
        # To check the condition whether the selected element is greater than the product of other remaining elements in the list,
        # if condition true the selected element is greatest    
        if (i>list_product):
            # Finally return the greater value from list
            return i
# Examples            
#Testcase 1
result=funList([10,3,50,4,2])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList([20,5,65,2,3])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList([15,10,1,5,100,2])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList([2,5,110,1,30])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funList([10,30,3,200,1])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=funList([100,2,15,2,20])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=funList([20,2,13,210,30])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=funList([30,50,4,320,1])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=funList([10,4,6,75,5])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=funList([10,50,1,2,510])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#

