'''
Write a function to take a dict, number numx and number Y as arguments. 
Multiply each key by number numx, each value by number Y. 
Finally iterate and return the new dict.
'''
#define function 
def funDict(org_dict,numx,numy):
    #define new dictionary
    new_dict={}
    #items gives list of tuples
    #iterates keys and values simantanuosly
    for i,j in org_dict.items():
        #updating nre dictionary keys multiply by x and valus multiply by y
        new_dict[i*numx]=j*numy
    #finally returns new dictionary    
    return new_dict
#calliing function
# finally print the new dictionary  
print(funDict({10:1,9:2,8:3,7:4,6:5,5:6,4:7,3:8,2:9,},3,4))   