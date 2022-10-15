'''Define a list of 10 elements. 
   If the element is even then multiply that element by 100,
   if the element is odd then multiply that element by 200. Finally print the new list
   :param orgList: to define list to stote the 10 elements inside the list by User
   return: from original list filter even and odd elements if it is even multiply by 100 
           if it is odd elements multiply by 200 finally return new list
solution steps:
1. Itertate original list = [1,2,3,4,10,12,16,20,30,11]
2. from the list filter which elements are even elements if it is even elements multiple by 100
3. from the list filter which elements are odd elements if it is odd elements multiple by 200
'''
# to store 10 elements into the original list
orgList = [10,20,30,101,110,210,220,310,40,50]
# define empty list
newList = []
# iterate original list
for i in orgList:
    # check if condition it true so even elements multiply by 100 
    # it is not true then it will goes to else condition
    if(i%2==0):
        # which elements multiply 100 those elements are add to the list
        newList.append(i*100)
        # odd elements are multiply by 200 
    else:
        # which elements are multiply by the 200 those elements are add to the new list
        newList.append(i*200)
# finally return new list
print(newList)