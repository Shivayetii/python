'''1.Write a function to take a list. Reverse and return the new list.
     :param orgDict: Original list passed by the User
     :return: Rerverse New list from orgList.
Example :
        listA=[10,20,30,40,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : [100,60,50,40,30,20,10]
'''
# function define the reverse the list
def fun_List(orgList):
  # define empty list
  newMapper = []
  # itearate the orginal list
  for i in reversed(orgList):
    # add elements in to new list
    newMapper.append(i)
  # finally return the new list
  return newMapper
# Execution
testList=[10,20,30,40,50,60,100]
result=fun_List(orgList=testList)
print("Final Result is :: {} ".format(result))