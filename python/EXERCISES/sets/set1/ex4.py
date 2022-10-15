'''Write a function to take a dict, number X as arguments. 
   If the dict key is > number X, then add it to new dict. 
   Finally iterate and return the new dict.
   :param orgDict: Original dictionary passed by the User
   :param numX: Number X passed by the User. Type is INT
    :return: return new dictionary
Solution Steps:
1. from the dictionary filter the which keys are greater than number X
2. add keys and values in new dictionary 
3. finally iterate new dictionary and return new dictionary
'''
# this function will define which keys are greater than numX
def funDict(orgDict,numX):
  # define empty dictionary
  new_Dict = {}
  # iterate original dictionary
  for key, value in orgDict.items():
    # this condition is checking for whick keys are greater than numX if it is true it will execute if statament
    if (key>numX):
      # add new keys and values to the new dictionary
      new_Dict[key] = value
  # iterate new dictionary keys and values
  for key, value in new_Dict.items():
    # print the new dictionary keys and values parllel
    print(key,value)
  # finally return new dictionary
  return new_Dict
# Execution
testDict={1:2,3:4,5:6,7:8,9:10}
numX=2
result=funDict(orgDict=testDict,numX=numX)
print("Final Result is :: {} ".format(result))