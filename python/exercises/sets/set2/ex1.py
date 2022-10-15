'''
Write a function to take a list and a number X as arguments.
From the list pick all numbers that are > er number X. 
Add those numbers to new list. Finally return the new list.
'''

#define function 
def fun_list(org_list,numx): 
    #define new empty list
    new_list=[]    
    #iterates original list elements on by
    for i in org_list:
        #checking for the condition is the element is grater than the number x
        if(i>numx):
            #adding elements to new list
            new_list.append(i)    
    #finally new list 
    return new_list 
 #calling function 
 # finally print the function  
print(fun_list([1,2,10,30,49],3))