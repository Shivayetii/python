
'''4.Write a function to take a dict as argument. 
     Sort the dict by keys and return the dict
     :param orgDict: Original dictionary passed by the User
     :return:the dictionary by keys and return the dict
   Example : 
            testDict={1:4,10:20,3:4,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {1:4,3:4,4:7,12:9,20:3,60:11}
solution steps:
1. Itertate  original dictionary keys = {1:4,10:20,3:4,4:7,60:11,12:9}
2. by using the sorted method to sort the original dictionary key elements
3. finally return the new dictionary
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
testDict={1:4,10:20,3:4,4:7,60:11,12:9}
result=funDict(orgDictsort=testDict)
print("Final Result is :: {} ".format(result))