'''Write a function to take a list and a number X as arguments.
   From the list pick all numbers that are > er number X. Add those numbers to new list. 
   Finally return the new list.
   :param orgList: Original list passed by the User
   :param numX: Number X passed by the User. Type is INT.
   :return: return new list

solution steps:
1. Itertate List original list = [1,3,5,7,9,10]
2. and then check the if condition in list pick the all numbers greater than number X
3. to add the elements which numbers are greater than number X to the empty list
4. finally return new list
'''
# this function is defined for the to pick all numbers in list which are greater than argumunt X
def fun_List(orgList,numX):
  # defined the empty list
  new_List = []
  # Iterrate original list
  for i in orgList:
    # this is checking the condition for which elements are greater than numX if it is true it will execute the 
    # if statement
    if (i>numX):
      # to add the elements to the new list
      new_List.append(i)
  return new_List
# Execution
testList=[1,3,5,7,9,10]
numX=3
result=fun_List(orgList=testList,numX=numX)
print("Final Result is :: {} ".format(result))
