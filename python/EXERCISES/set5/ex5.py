'''5.Write a function to take a dict as argument. Sort the dict by values and return the dict
   :param orgDict: Original dictionary passed by the User
   :return:the dict by values and return the dict
 Example : 
            testDict={1:4,10:20,3:40,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {1:4,4:7,12:9,60:11,10:20,3:40}'''
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
testDict={1:4,10:20,3:40,4:7,60:11,12:9}
result=funDict(orgDictsort=testDict)
print("Final Result is :: {} ".format(result))