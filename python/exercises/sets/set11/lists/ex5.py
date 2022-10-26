# Insert:
#  Adds a element at the specific index position

#Q1
listA=[5,8,9,4,3,3,7,2,1,6,10,15,3,3]
listA.insert(1,"Raj")
listA.insert(-2,"Sai")
listA.insert(-8,"yeti")
print(listA)
#Q2
listA=[1,2,6,7,3,4]
listB=[14,15,16,17]
listA.extend(listB)
listA.insert(2,100)
listA.append(listA[3] + listA[-1])
print(listA)