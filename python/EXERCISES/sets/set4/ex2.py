'''2.Write a function to take a list as an argument. 
     Find all the elements that occur in ODD indexes.
     :param orgList: Original list passed by the User
     :return: ODD indexes from list ONLY
 Example : 
        listA=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
        result=func_exec(listA)
        print(result)
        Expected Output : [2,4,6,2,9,100,2,10]
solution steps:
1. Itertate original lister = [1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
2. from the list to filter the odd indexes
3. finally return new list
'''
# This function gives a new list with odd index elements in the original list
def funList(orgList):
  # Define Empty list
  new_List = []
  # loop i variable contains odd indexes
  for index in range(1, len(orgList), 2):
    #elements adds to new list from original list which are in odd indexs
    new_List.append(orgList[index])
# finally returns a new list of ODD indexes 
  return new_List
# Execution
testList=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
result=funList(orgList=testList)
print("Final Result is :: {} ".format(result))
