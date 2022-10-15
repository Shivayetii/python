'''Write a function to take a dict, number X and number Y as arguments. 
   Multiply each key by number X, each value by number Y. 
   Finally iterate and return the new dict.
   :param orgDict: Original dictionary passed by the User
   :param numX: Number X passed by the User. Type is INT.
   :param numY: Number Y passed by the User. Type is INT
   :return: return new dictionary
Solution Steps:
1. dictionary Multiply each key by number X
2. dictionary Multiply each value  by number Y
3. finally iterate new dictionary and return new dictionary  
'''
# this function will define each key multiple by numX and each value is multiple by num Y and retuen new dictionary
# and iterate new dictionary parallel
def fun_Dict(orgDict,numX,numY):
  # define new dictionary
  new_Dict = {}
  # iterate original dictionary
  for key,value in orgDict.items():
    # each key is multiple by numX and each value multiple by numY and add new keys and values in new dictionary
    new_Dict[key*numX] = value*numY
  for key, value in new_Dict.items():
    print(key,value)
  return new_Dict
# Execution
testDict={1:2,3:4,5:6,7:8,9:10}
numX=2
numY=5
result=fun_Dict(orgDict=testDict,numX=numX,numY=numY)
print("Final Result is :: {} ".format(result))