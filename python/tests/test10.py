'''
Write a function to take a list. Select the number that is greater than sum of all other numbers.
    Example :
        listA=[1,2,13,4,5]
        result=func_exec(listA)
        print(result)
        Expected Output : 13
        Reason: 13 is greater than sum of [1,2,4,5] -> 12
    Example :
        listA=[100,20,300,40,1000,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : 1000
        Reason: 1000 is greater than sum of [100,20,300,40,50,60,100] 
'''
def funList(orgList):
    for ele in orgList:
        new_List=orgList
        new_List.remove(ele)
        if(ele>sum(new_List)):
            return ele
listA=[1,2,13,4,5]
result=funList(listA)
print(result)
listA=[100,20,300,40,1000,50,60,100]
result=funList(listA)
print(result)

def funList(orgList):
    for ele in orgList:
        if(ele[2]>sum(len(ele))):
            return ele
listA=[100,20,300,40,1000,50,60,100]
result=funList(listA)
print(result)

