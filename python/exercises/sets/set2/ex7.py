'''
    Write a function to take a list as an argument. 
    From the list pick the elements that are not divisible by 5. 
    Add those elements to new list. Finally return the new list.
'''
#define function
def funList(org_list):
    #define new empty list
    new_list=[]
    #iterates original eleents one by one
    for i in org_list:
        #checking for element not divisible by 5
        if (i%5!=0):
            #addind element to new list
            new_list.append(i)
    #finally return new list        
    return new_list
#calling function
# finally print the new list
print(funList([5,12,15,23,13,100]))               