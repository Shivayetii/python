'''6. Write a function to take 2 lists. 
      Iterate both the lists, if the elements in both the lists match then add it to new list.
      From that list select all elements in ODD indexes.Finally return the new list. 
      The new list must not contain duplicates.
    Example :
        listA=[10,20,30,40,50,60,100]
        listB=[10,200,30,40,500,60,100,400,90]
        result=func_exec(listA,listB)
        print(result)
        Expected Output : [30,100]
    Example :
        listA=[10,20,30,40,50,60,100]
        listB=[101,2001,130,140,1500,610,1100,4001,190,901]
        result=func_exec(listA,listB)
        print(result)
        Expected Output : []'''
# this function define orglistA and orglistB
def funList(orglistA,orglistB):
    #define an empty list
    Map_list=[]
    #define an empty list
    new_list=[]
    #iterates 2 different list Simantanously
    for (_key,_value) in zip(orglistA,orglistB):
        #checking for elements from both lists are equal if condition true element adds to new empty list
        if (_key==_value):
            #add element to new list   
            Map_list.append(_key)
    #checking for duplicates and loop is value contains even numbers                 
    for _key in range(1,len(Map_list),2):
        #checking for an element is not present already in new list if condition true an element is adds to new list
        if (_key not in new_list):
            #adding elements to new list     
            new_list.append(Map_list[_key])
    #finally return list without duplicates         
    return new_list
# Execution
testListA=[10,20,30,40,50,60,100]
testListB=[10,200,30,40,500,60,100,400,90]
result=funList(orglistA=testListA,orglistB=testListB)
print("Final Result is :: {} ".format(result))

