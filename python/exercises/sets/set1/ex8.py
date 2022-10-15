'''From the list pick the elements that are not EVEN. Add those elements to new list. 
   Finally print the new list'''

# to create original list and store 10 elements to the list
orgList = [1,2,3,4,5,6,7,8,9,10]
# define empty lisr
newList = []
# iterate new original list
for i in orgList:
    # to check the if condition which elements are not  even inside the list
    if(i % 2!=0):
        # add elements to the list
        newList.append(i)
# finally print the new list
print(newList)