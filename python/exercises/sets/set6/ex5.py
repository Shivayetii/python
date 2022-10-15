'''5. Write a function to take a dict and number X as argument. 
      Find the key,value pairs that are both divisible by number X
    Example : 
            testDict={10:20, 3:30, 4:40,90:100,20:30}
            numX=10
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {10:20,90:100,20:30}
    :param orgDict: Original dictionary passed by the User
    :param numX: Number X passed by the User. Type is INT.
    :return: Find the key,value pairs that are both divisible by number X and return new dictionary.
Solution Steps:
1. From the dictionary to Iterate the keys and values
2. To check the condition for items divisible by numberX
3. Return the new dictionary.
'''
# this function will define which keys and values are divisible by argument X
def funDict(orgDict,numX):
    # Define empty list
    new_Dict = {}
    # itarate the dictionary
    for key,value in orgDict.items():
        # this below the condition it will check which keys and which values are divisible by x if condition is true 
        # it will executes if statment
        if (key%numX==0 and value%numX==0):
            # this step will be demonstrate after divison of keys and values 
            # it will add new keys and new values new dictionary
            new_Dict[key] = value
    # finally returns a new list
    return new_Dict
# Execution
testDict={10:20, 3:30, 4:40,90:100,20:30}
numX=10
result=funDict(orgDict=testDict,numX=numX)
print("Final Result is :: {} ".format(result))