'''Write a function to take a list, number X as arguments. 
   From the list pick the elements that are not divisible by number X.
   Add those elements to new list. Finally return the new list.
'''
# this function will defined which elements inside that are not divisible by number X.
def funList(orgList,numX):
  # define empty list
  newList = []
  # iterate original list
  for i in orgList:
    # this is checking the condition for the inside that are not divisible by number X.
    if(i%numX!=0):
      # to add the new elements to the list
      newList.append(i)
  # finally return the new list
  return newList
# finally print the new list
print(funList([1,3,5,7,9,10],3))