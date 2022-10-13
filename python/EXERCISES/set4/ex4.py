'''4.Write a function to take a dict and number X arguments. 
   If the dict key is divisible by number X, then
   add the key to new dict and return the new dict.
   :param orgList: Original dictionary passed by the User
   :param numX: Number X passed by the User. Type is INT.
   :return: New dictionary with filtered values ONLY.
   Example : 
            testDict={1:4,10:20,3:4,4:7,60:11,12:9}
            numX=10
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {10:20,60:11}'''
#This function gives a new dictionary with key-value pair which the keys from original dictionary 
# is divisible by value x entered by the user
def funDict(orgDict,numX):
  # Define empty dictionary
  new_dict = {}
  #items method gives list of tuples from dictionary
  # iterates keys and  values from original dictionary
  for key,value in orgDict.items():
    #checking for is key divisible with value numx , if condition true the key and value is added to the new dictionary
    if (key%numX==0):
      #adding key-value pair to new dictionary
      new_dict[key] = value
  return new_dict
# Execution
testDict={1:4,10:20,3:4,4:7,60:11,12:9}
numX=10
result=funDict(orgDict=testDict,numX=numX)
print("Final Result is :: {} ".format(result))