'''
2. Write a function to take a list. Select the number that is greater than sum of all other numbers.
    Example :
        listA=[1,2,13,4,5]
        result=func_exec(listA)
        print(result)
        Expected Output : 13
        Reason: 13 is greater than sum of [1,2,4,5] -> 12
    Example :
        listA=[100,20,300,40,1000,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : 1000
        Reason: 1000 is greater than sum of [100,20,300,40,50,60,100] -> 670
        :param org_list: Original list passed by the User        
        :return: New list with filtered values ONLY
Solution Steps:
**************
Iterate the list -> listA:
    Find the current number, store in a variable currNumber
    Find the sum of remaining numbers and store in a variable sumList
    Check if currNumber is >er sumList:
        If yes:
            return currNumber
        else:
            continue the LOOP  
Finally return the new list        
'''
# This function is define pick greater number sum of all the list       
def funDict(org_list):

    # iterate the orginal list
    for i in org_list:
        # assigning org list to another variable like new_mapper 
        new_list=org_list
        # remove a selected element from the New list
        new_list.remove(i)
        # To check the condition whether the selected element is greater than the sum of other remaining elements in the list,
        # if condition true the selected element is greatest
        if (i>sum(new_list)):
            # Finally return the greater value from list
            return i
# Execution
testListA=[1,2,13,4,5]
#function calling
result=funDict(org_list=testListA)
#finally print result
print("Final Result is :: {} ".format(result))


# This function is define pick greater number sum of all the list       
def funDict(org_list):

    # iterate the orginal list
    for i in org_list:
        # assigning org list to another variable like new_mapper 
        new_list=org_list
        # remove a selected element from the New list
        new_list.remove(i)
        # To check the condition whether the selected element is greater than the sum of other remaining elements in the list,
        # if condition true the selected element is greatest
        if (i>sum(new_list)):
            # Finally return the greater value from list
            return i
# Execution
testListA=[100,20,300,40,1000,50,60,100]
#function calling
result=funDict(org_list=testListA)
#finally print result
print("Final Result is :: {} ".format(result))
