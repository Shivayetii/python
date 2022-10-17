'''
5. Write a function to take a dict as argument. Return the key that has max value.
        
    Example 1 : 
            testDict={10:20, 3:30, 4:16,90:100,20:31,11:23,17:44,20:400}
            result=func_exec(testDict)
            print(result)
            Expected Output : {20:400} 
            Reason:            
                400 is > 20
                400 is > 30
                400 is > 16
                400 is > 100
                400 is > 31
                400 is > 23
                400 is > 44
            :param org_dict: Original dictionary passed by the User
            :return: New dictionary with filtered values ONLY.      
                
    Solution steps:
    **************
    Take original dict and iterate key-value simantanously
        store values in _values
        checking for current key-value is greater than remaining 
        if Yes:
            add key-value to new dict
        else:
            continue loop
    Finally return new dict
'''
#define funtion
def funDict(org_dict):
    #define new dict
    new_dict={}
    #stores values in a list
    _values=org_dict.values()
    #iterates keys and values simantanously from original dict
    for _key,_value in org_dict.items():
        #checking for current key-value is greater than reamaining key-values
        if(_value==max(_values)):
            #updating new_dictionary
            new_dict[_key]=_value
   #finally returns new dict
    return new_dict
# Execution
#Example1
testDict={10:20, 3:30, 4:16,90:100,20:31,11:23,17:44,20:400}
result=funDict(org_dict=testDict)
print("Final Result is :: {} ".format(result))
# Execution
#Example2
testDict={10:20, 3:30, 4:16,90:10,20:31,11:23,17:44,20:40}
result=funDict(org_dict=testDict)
print("Final Result is :: {} ".format(result))