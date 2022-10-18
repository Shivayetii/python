'''5.Write a function to take a dict as argument. Sort the dict by values and return the dict
   :param orgDict: Original dictionary passed by the User
   :return:the dict by values and return the dict
 Example : 
            testDict={1:4,10:20,3:40,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {1:4,4:7,12:9,60:11,10:20,3:40}
Solution Steps:
**************
Define the  function 
  To define one empty dictionary
  Sort the dictionary value and store in variable
  Iterate the original dictionary = {1:4,10:20,3:40,4:7,60:11,12:9}
  Sorted values are add to the empty dictionary 
  Finally print the new dictionary              
'''
#This function returns new sorted dictionary by values
def funDict(orgDictsort):
  #values() method gives list of values
  #stores sorted list of values
  sorted_values = sorted(orgDictsort.values())
  # Define Empty dictionary
  sorted_dict = {}
  # Iterates values one by one
  for i in sorted_values:
    # iterates keys from original dict one by one
    for k in orgDictsort.keys():
    #checking for values and keys if condition true it adds to new dict.
       if orgDictsort[k] == i:
         #add key-value pair to new dictionary
         sorted_dict[k] = orgDictsort[k]
   # finally return the new dic 
  return sorted_dict
# Execution
#calling function
#Testcase 1
result=funDict({1:4,10:20,3:40,4:7,60:11,12:9})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funDict({1:4,10:20,3:40,4:7,60:11,12:9,4:3})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funDict({1:4,10:20,3:40,4:7,60:11,12:9,4:3,11:2})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funDict({1:4,3:40,4:7,60:11,12:9,4:3,11:1})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funDict({1:4,10:20,3:40,4:7,60:11,12:9,14:30,16:16})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funDict({1:4,10:20,3:40,4:7,60:11,12:9,17:18,1:1})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funDict({1:4,10:20,3:40,4:7,60:11,12:9,5:3,13:2})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funDict({1:4,10:20,3:40,4:7,60:11,12:9,13:50,16:40})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funDict({1:4,10:20,3:40,4:7,60:11,12:9,13:30,30:1})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funDict({1:4,10:20,3:40,4:7,60:11,12:9,40:1,50:3})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#