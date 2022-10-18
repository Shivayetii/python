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
def funDict(org_Dict):
    #define new dict
    new_Dict={}
    #stores values in a list
    values=org_Dict.values()
    #iterates keys and values simantanously from original dict
    for key,value in org_Dict.items():
        #checking for current key-value is greater than reamaining key-values
        if(value==max(values)):
            #updating new_dictionary
            new_Dict[key]=value
   #finally returns new dict
    return new_Dict
# Execution
#calling function
#Testcase 1
result=funDict({10:20, 3:30, 4:16,90:100,20:31,11:23,17:44,20:400})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funDict({10:20, 3:30, 4:16,90:10,20:31,11:23,17:44,20:40})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funDict({10:200, 3:30, 4:16,90:10,20:31,11:23,17:44,20:40})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funDict({10:20, 3:30, 4:16,90:100,20:31,11:23,17:44,20:40})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funDict({10:20, 3:30, 4:160,90:10,20:31,11:23,17:44,20:40})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funDict({10:20, 3:30, 4:16,90:10,20:31,11:230,17:44,20:40})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funDict({10:20, 3:300, 4:16,90:100,20:31,11:23,17:44,20:400})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funDict({10:20, 3:300, 4:16,90:100,20:31,11:23,17:44,20:400,30:500})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funDict({10:20, 3:300, 4:16,90:100,20:31,11:23,17:44,20:400})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funDict({10:20, 3:300, 4:16,90:100,20:31,11:23,17:44,20:400,40:600})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#