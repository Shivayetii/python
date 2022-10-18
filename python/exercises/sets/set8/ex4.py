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
def funDict(org_Dict):
    #deine new dict
    new_Dict={}
    #iterates keys and values simantanously
    for key,value in org_Dict.items():
      #checking for is value is divisible by key
      if(value%key==0):
        #add key and value to new dict
        new_Dict[key]=value
    #finally return new dict    
    return new_Dict
#Example1
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