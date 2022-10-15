'''Write a function to take a list as an argument. 
   From the list pick the elements that are not divisible by 5.
   Add those elements to new list. Finally return the new list.
   :param orgList: Original list passed by the User
   :return: return new list which elements are not divisible by 5.
solution steps:
1. Itertate original list = [1,3,5,7,9,10]
2. from the list filter which elements that are not divisible by 5.
3. finally return new list
'''
# this function will defined inside the list which elements are not divisible by 5.
def fun_List(Orglist):
  # define empty list
  new_List = []
  # iterate new list
  for i in Orglist:
    # this condition is checking for which elements not not divisible by 5. in side the list 
    # it is true it will execute if statement
    if(i%5!=0):
        # to add the new elements to the new list
        new_List.append(i)
  # finally return new list
  return new_List
# Execution
testList=[1,3,5,7,9,10]
numX=3
result=fun_List(orgList=testList,numX=numX)
print("Final Result is :: {} ".format(result))
