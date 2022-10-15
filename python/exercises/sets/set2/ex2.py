'''
Write a function to take a dict as an argument.
Multiply each key by 10, each value by 5. 
Finally iterate and return the new dict.
'''
#dfine function
def funDict(org_dict,x,y):
    #define new dictionary
    new_dict={}
    #items() gives list of tuples
    #loop iterats keys and values simantanously
    for i,j in org_dict.items():
        #updating new dictionary with key increases by x and each valuue by y
        new_dict[i*10]=j*5
    #finally returns new dictionary    
    return new_dict
#calling function
print(funDict({10:1,9:2,8:3,7:4,6:5,5:6,4:7,3:8,2:9,1:10},10,5))