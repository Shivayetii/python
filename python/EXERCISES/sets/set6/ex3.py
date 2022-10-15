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
        new_list=org_list
        # remove a selected element from the New list
        new_list.remove(i)
        # logic for product
        product=1
        for j in new_list:            
            product*=j
        # To check the condition whether the selected element is greater than the product of other remaining elements in the list,
        # if condition true the selected element is greatest    
        if (product):
            # Finally return the greater value from list
            return i
# Execution
testListA=[1,2,30,4,2]
#function calling
result=funList(org_list=testListA)
#finally print result
print("Final Result is :: {} ".format(result))

# This function is define pick greater number sum of all the list       
def funList(org_list):

    # iterate the orginal list
    for i in org_list:
        # assigning org list to another variable like new_mapper 
        new_list=org_list
        # remove a selected element from the New list
        new_list.remove(i)
        # logic for product
        product=1
        for j in new_list:            
            product*=j
        # To check the condition whether the selected element is greater than the product of other remaining elements in the list,
        # if condition true the selected element is greatest    
        if (product):
            # Finally return the greater value from list
            return i
# Execution
testListA=[1,2,3,4,2]
#function calling
result=funList(org_list=testListA)
#finally print result
print("Final Result is :: {} ".format(result))
