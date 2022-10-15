'''1. Write a function to take a list as an argument. Find the number that occurs the most number of times.
    Example1 : 
        org_list=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
        result=func_exec(org_list)
        print(result)
        Expected Output : {2:3} 
        Reason: Number 2 occurs 3 times in the list
        org_list=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10,1,1]
        result=func_exec(org_list)
        print(result)
        Expected Output : {2:3, 1:3} 
        Reason: Number 2 occurs 3 times in the list and number 1 also occurs 3 times
        org_list=[1,2,300,4,5,6,7,10,11,21,80,900]
        result=func_exec(org_list)
        print(result)
        Expected Output : "NULL"
        Reason: All numbers in the list occur exactly once, so result in "NULL"
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY
solution steps:
1. Itertate original lister = [1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
2. from the list to find the most occurence 
3. finally return new dictionary
'''
#This Function gives the most repeated elements from the list
def fun_Dict(org_list):
    #define an empty dictionary
    new_Dict={}
    #iterares original list
    for i in org_list:
        #checking for count is the element present in the original list more than 1 
        if (org_list.count(i)>1):
            #checking for element is not present in the dictionary with name new_mapping
            if (i not in new_Dict):
                #updating  dictionary name new_mapping , i as key refers to element most repeated and value refers to how many number of times repeated the element
                new_Dict[i]=org_list.count(i)
    #checking for is the new_mapping dictionary is empty, if condition true return Null           
    if (new_Dict=={}):
        # return null
        return 'NULL'
    #stores values from dictionary new_mapping
    val=new_Dict.values()    
    #items() method on dictionary gives list tupltuples
    #iterates dictionary i contains keys and j contains values  
    for i,j in new_Dict.items():
        #checking for value of j is maximum element in the list val, if condition true it returns the dictionary with key as element in the list most repeated and values as number of times element repeated
        if (j==max(val)):
            #finally return with dictionary format
            return {i:j}  
# Execution
testList=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
#function calling
result=fun_Dict(org_list=testList)
#finally print result
print("Final Result is :: {} ".format(result))
# Example2
testList=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10,1,1]
#function calling
result=fun_Dict(org_list=testList)
#finally print result
print("Final Result is :: {} ".format(result))
# Example3
testList=[1,2,300,4,5,6,7,10,11,21,80,900]
#function calling
result=fun_Dict(org_list=testList)
#finally print result
print("Final Result is :: {} ".format(result))