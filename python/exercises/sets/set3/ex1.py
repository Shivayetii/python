'''1. Write a function to take a list as an argument. Remove all duplicates from the list. 
Don't use any built-in. Check using if conditions.
    Example : 
        listA=[1,2,3,4,5,6,7,8,9,10,11,12,1,1,2,4,4,5,6,7]
        result=func_exec(listA)
        print(result)
        Expected Output : [1,2,3,4,5,6,7,8,9,10,11,12]
        :param orgList: Original list passed by the User
        :return: New list with filtered values ONLY
        '''
#This function removes duplicates elements from list
def funList(orgList):
    #Define an empty new list
    new_list=[] 
    # itarate the list
    for i in orgList:
        #checking for an element is in an empty list, if an element is present it ignored as a duplicate
        if (i not in new_list):
            #elements add to new list
            new_list.append(i) 
    #finally returns a new list without duplicates
    return new_list 
# Execution
testList=[1,2,3,4,5,6,7,8,9,10,11,12,1,1,2,4,4,5,6,7]
result=funList(orgList=testList)
print("Final Result is :: {} ".format(result))
