'''Write a function to take a dict as an argument. Multiply each key by 10, each value by 5. 
   Finally iterate and return the new dict.
   :param orgDict: Original dictionary passed by the User
   :param numX: Number X passed by the User. Type is INT.
   :param numY: Number Y passed by the User. Type is INT
   :return: return new dictionary

Solution Steps:
1. dictionary Multiply each key by 10
2. dictionary Multiply each key by 5
3. finally iterate new dictionary and return new dictionary
'''
# this function will define each key multiple by numX and each value is multiple by num Y and retuen new dictionary
# and iterate new dictionary parallel
def fun_Dict(orgDict):
  # define empty dictionary
  new_Dict = {}
  # iterate original dictionary
  for key,value in orgDict.items():
    # multiple each key with 10 and multiple each value with 5 and add the new keys and values are
    # add to the new dictionary
    new_Dict[key*10] = value*5
  # iterate new dictionary
  for key, value in new_Dict.items():
    # to print the new key and values of new dictionary in parallel
    print(key,value)
  # finally return new dictionary
  return new_Dict
# Execution
print(fun_Dict({1:4,3:9,2:6,10:7,19:10,11:12}))