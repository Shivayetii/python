
'''From the list pick the elements that are not ODD. 
   Add those elements to new list. Finally print the new list
   :param orgList: to define list to stote the 10 elements inside the list by User
   :return: finally return new list 
solution steps:
1. Itertate original list = [10,20,30,101,110,210,220,310,40,50]
2. from the list filter odd elements
3. finally return new list
'''
# to store 10 elements into the original list
orgList = [1,2,3,4,5,6,7,10,30,40]
# define empty list
newList = []
# iterate original list
for i in orgList:
    # this is checking condition for inside the list which elements are not odd elements
    if(i %2== 0):
        # to add new elements inside the list which elements are not odd elements
        newList.append(i)
# finally return or print the new list
print(newList)