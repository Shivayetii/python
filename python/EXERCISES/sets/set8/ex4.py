'''
4. Write a function to take a dict as argument.
If the dict-val is the divisible by dict-key then filter, add to new dict.
Finally return the new dict.
      
  Example 1 : 
      testDict={10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400}
      result=func_exec(testDict)
      print(result)
      Expected Output : {10:20,3:30,4:16,20:400}
      
      Reason: 
            20 is divisible by 10
            30 is divisible by 3
            16 is divisible by 4
            400 is divisible by 20
      :param org_dict: Original dictionary passed by the User
      :return: New dictionary with filtered values ONLY.  
  Solution Steps:
  **************
  Take a dict and iterate keys and values simantanously
  checking for value is divisible by key
    if Yes:
      add key and value to new dict
    else
      continue loop
  Finally return new dict              
'''
#define function
def funDict(orgDict):
    #deine new dict
    new_dict={}
    #iterates keys and values simantanously
    for _key,_value in orgDict.items():
      #checking for is value is divisible by key
      if(_value%_key==0):
        #add key and value to new dict
        new_dict[_key]=_value
    #finally return new dict    
    return new_dict
# Execution
testDict={10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400}
result=funDict(orgDict=testDict)
print("Final Result is :: {} ".format(result))
