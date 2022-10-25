# Index: 
# Position of element or an item in a string of characters called index
# Index start from 0 and reverse position start from -1
# List will allow the duplicates
#Q1
listA = [4, 1, 5, 3, 10,40]
print(listA.index(10))
print(listA.index(4))
#Q2 
list1 = ["shiva","yeti","sai","raj"]
print(list1.index("shiva"))
print(list1.index("yeti"))

#Q3
list1 = [1,2,3,5,6]
list2 = [10,20,30,40]
list1.append(list2)
print(list1)
print(list1.index(5))
print(list1.index(6))
#Q4
list1 = [1,2,3,5,6]
list2 = [10,20,30,40]
list1.append(list2)
print(list1)
print(list1.index(5))
print(list1.index(6))
#Note getting value error
print(list1.index(10))
#Note getting value error
print(list1.index(20))

#Q5
list1 = [1,2,3,5,6]
list2 = ["shiva","yeti","sai","raj"]
list1.append(list2)
print(list1)
print(list1.index(5))
print(list1.index(6))
#Note getting value error
print(list1.index("yeti"))
#Note getting value error
print(list1.index("shiva"))
