'''
    2. Write a function to take a list argument. Find the elements that has greatest length.
    Example 1 :
        listA=["hello","world","science","maths","Python"]
        result=func_exec(listA)
        print(result)
        Expected Output : ["science"]
        Reason: length of science -> 7
    Example 2 :
        listA=["hello","world","science","maths","Pythonics"]
        result=func_exec(listA)
        print(result)
        Expected Output : ["Pythonics"]
        Reason: length of Pythonics -> 9
    Example 3 :
        listA=["hello","world","today"]
        result=func_exec(listA)
        print(result)
        Expected Output : []
        Reason: All lengths are same.
        Length of hello -> 5
        Length of world -> 5
        Length of today -> 5
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY.  
        
    Solution Steps:  
    **************
    Take original list and iterate
        Store sizes of words in a list 
        checking if the word size is greater than remaining words
        if yes:
            add to new list
        else:
            continue loop
    check for new list contains only one word
    if yes:
        return new list
    else:
        retuen empty list []                
'''
#define function 
def fun_list(org_list):
    #define new list 
    new_list=[]
    #define list to store lengths of elements in orginal list
    len_list=[]
    #iterate original list
    for i in org_list:
        #adding lengths   to lengths list
        len_list.append(len(i))
    #iterate orginal list
    for j in org_list:
        if(len(j)==max(len_list)):
            new_list.append(j)    
    #checking for is element in new list one ,if new list contains more than one returns empty list
    if(len(new_list)==1):
        return new_list
    else:
        return [] 
# Execution
testList=["hello","world","science","maths","Python"]
result=fun_list(org_list=testList)
print("Final Result is :: {} ".format(result))

# Example2
testList=["hello","world","science","maths","Pythonics"]
result=fun_list(org_list=testList)
print("Final Result is :: {} ".format(result))

# Example3
testList=["hello","world","today"]
result=fun_list(org_list=testList)
print("Final Result is :: {} ".format(result))
