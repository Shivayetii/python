'''Define a list of 10 elements. From the list pick all numbers that are > er 100. 
   Add those numbers to new list. Finally print the new list.
   :param orgList: to define list to stote the 10 elements inside the list by User
   :return: return new list which elements are greater than 100
solution steps:
1. Itertate original list = [10,20,30,101,110,210,220,310,40,50]
2. from the list filter which elements that greater than 100
3. finally return new list
'''
# to store 10 elements into the original list
orgList = [10,20,30,101,110,210,220,310,40,50]
# define empty list
newList = []
# iterate original list
for i in orgList:
    # this is checking condition for inside the list which elements are greater than 100
    if(i>100):
        # to add new elements inside the list which elements are greater than 100 to the new list 
        newList.append(i)
# finally return or print the new list
print(newList)