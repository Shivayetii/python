'''Define a list of 10 elements. 
   From the list pick the elements that are not divisible by 5 and 3. 
   Add those elements to new list. Finally print the new list.'''
# to create original list and store the 10 elements into the list
orgList=[8,9,5,7,3,2,1,6,4,10]
# to define empty list
newList=[]
# iterate original list
for i in orgList:
  # this is checking the condition for which elements are not divisible by 5 and 3.
  if(i % 3 !=0) and (i % 5!=0):
    # to the new elements to the list
    newList.append(i)
# finally print the new list
print(newList)    