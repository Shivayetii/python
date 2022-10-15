'''Write a function to take a list as an argument. 
   If the element is even then multiply that element by 100, if the element is odd then 
   multiply that element by 200. Finally return the new list.'''
# this function is defined for the if elements is evene multiple by 100 and it is odd multiple by 200
def funDict(orgList):
    # define empty list
    new_list = []
    # iterate original list
    for i in orgList:
        # this is checking the condition for if the elements even that element multiply by 100 it is not true 
        # it is goes to the else block
        if(i%2==0):
            # even elements are add to the new list
           new_list.append(i*100)
        # it will filter the odd elements its odd multiply by 200
        else:
          # odd elements are add to the new list
          new_list.append(i*200)
    # finally return the new list
    return new_list
# finally print the new list
print(funDict([1,3,5,7,9,10,12,15,20,25],3))