'''
2. Write a function to take a list. Select the number that is greater than sum of all other numbers.
    Example :
        listA= [1,2,13,4,15]
        result=func_exec(listA)
        print(result)
        Expected Output : []
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
'''
3. Write a function to take a list. Select the number that is greater than product of all other numbers.
    
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