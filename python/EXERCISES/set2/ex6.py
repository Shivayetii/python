'''Define a list of 10 elements. From the list pick the elements that are not divisible by 5 and 3. 
Add those elements to new list.
 Finally print the new list'''
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = []
for i in l1:
    if(i % 3 != 0) and (i % 5!=0):
        l2.append(i)
print(l2)