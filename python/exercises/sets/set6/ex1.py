'''1. Write a function to take a list. Filter all the prime numbers, add to new list and return the new list.
    Example :
        org_list=[10,20,30,40,50,60,100,11]
        result=func_exec(org_list)
        print(result)
        Expected Output : [11]
    Example :
        org_list=[10,20,23,30,40,50,60,100,11]
        result=func_exec(org_list)
        print(result)
        Expected Output : [11,23]
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY.
Solution Steps:
1. From the list, checking for number is greater than Or equals to 2
2. checking prime numbers from the list
2. Iterate the list and add to the new list
3. Return the prime list
'''
#This Function return prime number list
def funList(orgList):
    #define new list
    new_List=[]
    #iterates original list one by one
    for i in orgList:
        #checking for number is greater than Or equals to 2
        if(i>=2):        
            #every prime has 2 co-factors 1 and it self number, we are taking range from 2 to one less the number
            # if we found any co-factors between these range this is a prime number        
            for j in range(2,i):
                #checking for Divisiblity if condition true loop will break
                if(i%j==0):
                    #breakdown loop
                     break        
            else:
                    #if loop not breakable the number is prime and adds to new list
                    new_List.append(i)    
    #finally return                        
    return new_List
#Execution
#calling function
#Testcase 1
result=funList([10,20,30,40,50,60,100,11])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList([10,20,30,40,50,60,100,13])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList([10,20,30,40,50,60,100,13,11])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList([10,20,30,40,50,60,100,23,29])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funList([10,20,30,40,50,60,100,13,83,89])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funList([10,20,30,40,50,60,100,13,83,89,51,53])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funList([10,20,30,40,50,60,100,13,37,39])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funList([10,20,30,40,50,60,100,13,53,57])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funList([10,20,30,40,50,60,100,13,83,101,103])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funList([10,20,30,40,50,60,100,13,113,117])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#