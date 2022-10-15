'''
    Write a function to take a list as an argument. 
    If the element is even then multiply that element by 100, 
    if the element is odd then multiply that element by 200. Finally return the new list.
'''
#define function
def funList(org_list,x,y):
    #define new list
    new_list=[]
    #iterates all elements  in the  oriinal list one by one    
    for i in org_list:
        # checking for if the elements is even
        if (i%2==0):
            new_list.append(i*100)
        else:
            new_list.append(i*200)
    #finally return new list        
    return new_list
#calling function
print(([11,100,127,99,128,331,990,23,68,10],100,200))
   