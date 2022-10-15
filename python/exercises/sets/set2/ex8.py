'''
    Write a function to take a list, number X as arguments. 
    From the list pick the elements that are not divisible by number X. 
    Add those elements to new list. Finally return the new list.
'''
#define function
def funList(org_list,x):
    #define new list
    new_list=[]
    #iterates elements from original list one by one
    for i in org_list:
        #checking for element not divisible by number x
        if (i%x!=0):
            #add new list
            new_list.append(i)
    #finally return new list        
    return new_list
#calling function
print(funList([12,4,45,89,99,100,50],5))