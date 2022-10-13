'''3. Write a function to take a list. Select the number that is greater than product of all other numbers.
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
Solution Steps:
1. First from List we need to check which indesx have large value in the List
2. multiple the smallest indexes in the list
3. Check the codition of multiple the smallest indexes in the list is greater than largest index number
'''
# thsi function is defined for multiple of the smallest indexes in the list is greater than largest index number
def funList(orgList):
  # product of the smallest indexes in the list
  product = orgList[0]*orgList[1]*orgList[3]*orgList[4]
  # it will demonstrate maximum index value in the list
  max_value = orgList[2]
  # iterate list
  for product in orgList:
    # it will check the condition product of  the smallest indexes in the list is greater than largest index number
    # if condition is true it will execute if statment
    if(product > max_value):
       # it will check maximim value of index equal to product of  the smallest indexes values in the list
      max_value = product
  # finally return maximum in list
  return max_value
#Execution
testList=[1,2,30,4,2]
#function calling
result=funList(orgList=testList)
#finally print result
print("Final Result is :: {} ".format(result)) 

