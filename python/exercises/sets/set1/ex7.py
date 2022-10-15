'''Write a function to take a list as an argument. 
   From the list pick the elements that are not divisible by 5. 
   Add those elements to new list. Finally return the new list.
'''
# this function is defined for which elements that are not divisible by 5.
def funList(orgList):
     # define empty list
     newList = []
     # iterate original list
     for i in orgList:
        # this checking the condition for which elements are not divisible by 5
        if(i%5!=0):
            # add new elements to the list
            newList.append(i)
     # finally return new list
     return newList
# finally print the new list
print(funList([1,3,5,7,9,10,12,15,20,25]))