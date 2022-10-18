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
def funList(org_List):
    #define new list 
    new_List=[]
    #define list to store lengths of elements in orginal list
    len_List=[]
    #iterate original list
    for i in org_List:
        #adding lengths   to lengths list
        len_List.append(len(i))
    #iterate orginal list
    for j in org_List:
        if(len(j)==max(len_List)):
            new_List.append(j)    
    #checking for is element in new list one ,if new list contains more than one returns empty list
    if(len(new_List)==1):
        return new_List
    else:
        return [] 
# Execution
#calling function
#Testcase 1
result=funList(["hello","world","science","maths","Python"])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList(["hello","world","science","maths","Pythonics"])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList(["hello","world","today"])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList(["hello","world","today","python"])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funList(["hello","world","today","yesterday","exercisesexamples",""])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funList(["hello","sets","quires"])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funList(["hello","sets","quires","assignments"])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funList(["dictionaries","sets","quires","assignments"])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funList(["functions","sets","quires"])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funList(["functions with arguments","sets","quires"])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#

