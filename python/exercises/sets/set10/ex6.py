'''Write a function to take a dict as argument. 
	If the dict-val is the divisible bydict-key then filter, add to new dict.
   Finally return the new dict.

	Example : 
			testDict={10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400}
			result=func_exec(testDict)
			print(result)
			Expected Output : {10:20,3:30,4:16,20:400}
			Reason: 
				20 is divisible by 10
				30 is divisible by 3
				16 is divisible by 4
				400 is divisible by 20
Solution Steps:
**************
Iterate Original dictionary of keys and values
Check if condition is  dict-val is the divisible by dict-key 
  If Yes:
    add to new dictionary
  else:
    continue loop
Finally return the new dictionary 
'''

# Define the function
def funDict(org_dic):
    # Define the empty dictionary
    new_dic={}
    # Iterate the dictionary keys and values
    for key,value in org_dic.items():
        # Check the condition for dict-val is the divisible by dict-key  
        if (value%key==0):
            # update the new dictionary
            new_dic[key]=value
    # Finally return the new dictionary        
    return new_dic

# Execution
#calling function
#Testcase 1
result=funDict({10:20, 3:30, 4:16,90:100,20:30,11:23,17:44,20:400})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funDict({1:2,3:10,10:20,30:10})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funDict({30:40,40:300,2:1,1:100})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funDict({1:10,20:10,30:40,3:200})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funDict({3:2,4:1,45:31,72:9,14:13})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=funDict({3:5,4:3,5:8,9:5,9:2,12:17})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=funDict({12:21,16:61,14:41,17:34,13:31,68:51})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=funDict({10:42,16:7,5:20,7:14,10:6,12:30})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=funDict({5:10,10:3,3:9,9:10})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=funDict({10:10,20:20,11:9,23:11})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")