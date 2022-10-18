'''
3. Write a function to take a dict as argument. 
If the dict-key and dict-val are both PRIME then filter, add to new dict.
Finally return the new dict.
   Example 1 : 
        testDict={10:20, 3:30, 4:40,90:100,20:30,11:23,17:44}
        result=func_exec(testDict)
        print(result)
        Expected Output : {11:23}
        :param org_dict: Original dictionary passed by the User
        :return: New dictionary with filtered values ONLY.  
        
   Solution Steps:
   **************
   Take a dict and iterate keys and values both simantanously        
   checking for co-factors if found any co-factors between these range loop will break
        if yes:
           loop will break
        else:
           add the new dictionary
  Finally return new dict                    
''' 
#define function
def funDict(org_Dict):
        #define new dict
        new_Dict={}        
        #itrates keys and values simantanously
        for key,value in org_Dict.items():
                #loop for checking key is prime
                for k in range(2,key):
                        #checking for co-factors if found any co-factors between these range loop will break
                        if(key%k==0 or key<2):
                          break
                else:
                        #checking for value is prime
                        for l in range(2,value):
                                #if found any co-factors between these range loop will break
                                if(value%l==0 or value<2):
                                         break   
                        else:
                                #both key and value prime,so add to new dictionary
                                 new_Dict[key]=value     
         #finally return new dictionary               
        return new_Dict      
# Execution
#calling function
#Testcase 1
result=funDict({10:20, 2:3, 4:16,90:100,20:31,11:23,17:44,20:400})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funDict({10:20, 41:43, 4:16,90:10,20:31,5:7,17:44,20:40})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funDict({23:29, 3:30, 4:16,53:59,20:31,11:23,17:44,20:40})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funDict({10:20, 3:30, 4:16,90:100,20:31,11:23,17:19,29:31})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funDict({10:20, 3:30, 83:79,90:100,20:31,11:23,17:19,29:31})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funDict({107:109, 109:113, 4:16,90:100,20:31,11:23,17:19,29:31})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funDict({10:20, 3:30, 23:29,90:100,20:31,11:23,17:19,29:31})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funDict({10:20, 3:30, 4:16,89:97,20:31,11:23,17:19,29:31})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funDict({10:20, 3:30, 4:16,67:61,20:31,11:23,17:19,29:31})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funDict({10:20, 127:131, 149:151,90:100,20:31,11:23,17:19,29:31})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
