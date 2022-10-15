'''2.Write a function to take a list. Sort and return the new list.
   :param orgDict: Original list passed by the User
   :return: sorted New list from orgList.
Example :
        listA=[100,20,300,40,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : [20,40,50,60,100,100,300]
solution steps:
1. Itertate  original listA = [100,20,300,40,50,60,100]
2. by using the sorted method to sort the original list elements
3. finally return the new list
'''
# define function for sorted the list
def fun_List(orgList):
  # Define Empty list
  newMapper = []
  # sort the orginal list
  for i in sorted(orgList):
    # add the elements in new list
    newMapper.append(i)
  #Finally return new sorted list 
  return newMapper
# Execution
testList=[100,20,300,40,50,60,100]
result=fun_List(orgList=testList)
print("Final Result is :: {} ".format(result))



