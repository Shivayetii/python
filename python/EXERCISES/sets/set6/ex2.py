'''2. Write a function to take a list. Select the number that is greater than sum of all other numbers.
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
        :param listA: List passed by the User
        :param: Select the number that is greater than sum of all other numbers in side the list.
        :return: Get out put as the greater than sum of [1,2,4,5] -> 12

Solution Steps:
1. First from List we need to check which indesx have large value in the List
2. Sum the smallest indexes in the list
3. Check the codition of Sum the smallest indexes in the list is greater than largest index number
'''
# thsi function is defined for sum the smallest indexes in the list is greater than largest index number
def funList(orgList):
  # Sum of the smallest indexes in the list
  sum = orgList[0]+orgList[1]+orgList[3]+orgList[4]
  # it will demonstrate maximum index value in the list
  max_value = orgList[2]
  # iterate list
  for sum in orgList:
    # it will check the condition sum the smallest indexes in the list is greater than largest index number
    # if condition is true it will execute if statment
    if(sum > max_value):
      # it will check maximim value of index equal to sum of  the smallest indexes values in the list
      max_value = sum
  # finally return maximum value in the list
  return max_value
#Execution
testList=[1,2,13,4,5]
#function calling
result=funList(orgList=testList)
#finally print result
print("Final Result is :: {} ".format(result))  

# thsi function is defined for sum the smallest indexes in the list is greater than largest index number
def funList(orgList):
  # Sum of the smallest indexes in the list
  sum = orgList[0]+orgList[1]+orgList[2]+orgList[3]+orgList[5]+orgList[6]+orgList[7]
  # it will demonstrate maximum index value in the lis
  max_value = orgList[4]
  # iterate list
  for sum in orgList:
    # it will check the condition sum the smallest indexes in the list is greater than largest index number
    # if condition is true it will execute if statment
    if(sum > max_value):
      # it will check maximim value of index equal to sum of  the smallest indexes values in the list
      max_value = sum
  #finally print result
  return max_value
#Execution
testList=[100,20,300,40,1000,50,60,100]
#function calling
result=funList(orgList=testList)
#finally print result
print("Final Result is :: {} ".format(result))  

      
    
      
    