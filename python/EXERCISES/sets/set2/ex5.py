'''Define a list of 10 elements. 
   From the list pick the elements that are not divisible by 5. 
   Add those elements to new list. Finally print the new list.
   :param orgList: to define list to stote the 10 elements inside the list by User
   :return: finally return new list 
solution steps:
1. Itertate original list = [10,20,30,101,110,210,220,310,40,50]
2. from the list filter which elements are not divisible by 5.
3. finally return new list
'''
# to store 10 elements into the original list
orgList = [10,20,30,101,110,210,220,310,40,50]
# define empty list
newList = []
# iterate original list
for i in orgList:
    # this is checking condition for inside the list which elements are not divisible by 5.
    if(i%5!=0):
        # to add new elements inside the list which elements are greater than 100 to the new list 
        newList.append(i)
# finally return or print the new list
print(newList)