'''
        7.Write a function to take a dict as argument. Sort the dict by values and return the dict
        Example : 
                    testDict={1:4,10:20,3:40,4:7,60:11,12:9}
                    result=func_exec(testDict)
                    print(result)
                    Expected Output : {1:4,4:7,12:9,60:11,10:20,3:40}
        :param orgDict: Original dictionary passed by the User
        :return:the dict by values and return the dict
            Given:
              testDict={1:4,10:20,3:40,4:7,60:11,12:9}
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
  for val_1 in sorted_values:
    # iterates keys from original dict one by one
    for val_2 in orgDictsort.keys():
    #checking for values and keys if condition true it adds to new dict.
       if orgDictsort[val_2] == val_1:
         #add key-value pair to new dictionary
         sorted_dict[val_2] = orgDictsort[val_2]
   # finally return the new dic 
  return sorted_dict