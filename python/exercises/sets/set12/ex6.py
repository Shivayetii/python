
'''6.Write a function to take a dict as argument. Sort the dict by keys and return the dict
    Example : 
            testDict={1:4,10:20,3:4,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {1:4,3:4,4:7,12:9,20:3,60:11}
    :param orgDict: Original dictionary passed by the User
    :return:the dictionary by keys and return the dict
         Given:
              {1:4,10:20,3:4,4:7,60:11,12:9}
		      Expected Output : {1:4,3:4,4:7,12:9,20:3,60:11}
              
    Solution Steps:
    **************
    Define the function 
    To define one empty dictionary
    Iterate the original dictionary = {1:4,10:20,3:4,4:7,60:11,12:9}
    Sort the original dictionary  keys
    Sorted original dictionary  keys are add to the empty dictionary 
    Finally print the new dictionary       
'''
#This function returns new sorted dictionary
def funDict(orgDictsort):
  #define empty dictionary
  sorted_dict={}
  #sorted method on dictionary gives a list with sorted keys
  #iterates keys from least to maximum
  for key in sorted(orgDictsort):
    #adds key-value pair to new dictionary
    sorted_dict[key]=orgDictsort[key]
  #finally return the new dic    
  return sorted_dict
# Execution
#calling function
#Testcase 1
result=funDict({1:4,10:20,3:4,4:7,60:11,12:9})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funDict({1:4,10:20,3:4,4:7,60:11,12:9,20:30})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funDict({1:4,10:20,3:4,4:7,60:11,12:9,14:200,17:300})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funDict({1:4,10:20,3:4,4:7,60:11,12:9,14:200,7:300})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funDict({1:4,10:20,3:4,4:7,60:11,12:9,5:9,9:20})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funDict({1:4,10:20,3:4,4:7,60:11,12:9,55:50,8:9})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funDict({1:4,10:20,3:4,4:7,60:11,12:9,55:50,8:9,8:100,15:200})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funDict({5:4,10:20,1:4,4:7,60:11,12:9,55:50,8:9,8:100,15:200})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funDict({1:4,10:20,3:4,4:7,60:11,12:9,55:50,8:9,5:100,9:200})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funDict({2:4,10:20,3:4,4:7,60:11,12:9,51:50,8:9,5:100,19:200})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#