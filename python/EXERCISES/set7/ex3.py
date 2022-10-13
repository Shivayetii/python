'''3. Write a function to take a list. From the list find the number that occurs most number of times.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        result=func_exec(listA)
        print(result)
        Expected Output : []
    Example :
        listA=[10,21,30,41,50,500,100,11,12,13,21]
        result=func_exec(listA)
        print(result)
        Expected Output : [21,]
         Example :
        listA=[10,21,30,41,50,50,100,11,12,13,21]
        result=func_exec(listA)
        print(result)
        Expected Output : [21,50]
       :param org_list: Original list passed by the User
       :return: New list with filtered values ONLY.  
Solution Steps:
1. Iterate the list and check condition for most repeated element in the list
2. Remove the duplicates
3. Add elelments into new list and return

'''