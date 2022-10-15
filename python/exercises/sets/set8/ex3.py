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
def funDict(org_dict):
        #define new dict
        new_dict={}        
        #itrates keys and values simantanously
        for _key,_value in org_dict.items():
                #loop for checking key is prime
                for k in range(2,_key):
                        #checking for co-factors if found any co-factors between these range loop will break
                        if(_key%k==0 or _key<2):
                          break
                else:
                        #checking for value is prime
                        for l in range(2,_value):
                                #if found any co-factors between these range loop will break
                                if(_value%l==0 or _value<2):
                                         break   
                        else:
                                #both key and value prime,so add to new dictionary
                                 new_dict[_key]=_value     
         #finally return new dictionary               
        return new_dict      
#calling function
# Execution
#Example1
testDict={10:20, 3:30, 4:40,90:100,20:30,11:23,17:44}
result=funDict(org_dict=testDict)
print("Final Result is :: {} ".format(result))
#Example2
testDict={10:20, 3:30, 4:40,90:100,20:30,11:23,17:44,7:17}
result=funDict(org_dict=testDict)
print("Final Result is :: {} ".format(result))
