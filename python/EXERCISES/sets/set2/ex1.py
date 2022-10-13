'''Define a list of 10 elements. From the list pick all numbers that are > er 100. 
Add those numbers to new list. 
Finally print the new list.'''
l1 = [10,20,30,101,110,210,220,310,40,50]
l2 = []
for i in l1:
    if(i>100):
        l2.append(i)
print(l2)