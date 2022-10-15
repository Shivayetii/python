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
def funList(org_list):
    #define new list
    new_List=[]
    #iterates original list one by one
    for i in org_list:
        #checking for number is greater than Or equals to 2
        if(i>=2):        
            # below the will check the prime numbers within the list prime is nothing which elements not divisible 2    
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
testList=[10,20,30,40,50,60,100,11]
#function calling
result=funList(org_list=testList)
#finally print result
print("Final Result is :: {} ".format(result))    