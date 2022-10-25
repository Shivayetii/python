#  Sorting:
# Ascending order of elememnts like numbers and alphabets
#Q1
listA=[10,1,3,2,4,30,19,17]
listB=["shiva","yeti","sai","raj"]
print(sorted(listA))
print(sorted(listB))
#Q2
listA=[10,1,3,2,4,30,19,17]
listB=["shiva","yeti","sai","raj"]
listA.extend(listB)
print(listA)
# both string and integer are not supported for sorted
print(sorted(listA))