# Deletion:
# Specify the item to be deleted by index.

listA=[1,2,3,4,5,6,7,8,9,10]
del listA[4]
print(listA)
listB = [1,2,3,4,5,6,7,8,9,10]
del listB[-1]
print(listB)
listC= [1,2,3,4,5,6,7,8,9,10]
del listC[:2] 
print(listC)
listD=[1,2,3,4,5,6,7,8,9,10]
del listD[3:]
print(listD)
listE = [1,2,3,4,5,6,7,8,9,10]
del listE[2:6]
print(listE)
listF=[1,2,3,4,5,6,7,8,9,10]
del listF[:] 
print(listF)

