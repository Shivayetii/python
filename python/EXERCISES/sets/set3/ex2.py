'''2. Write a function to take a dict as an argument. Find the key that has maximum value and return the key.
    Example : 
        testDict={1:4,10:100,3:90,4:40,6:80,12:200}
        result=func_exec(testDict)
        print(result)
        Expected Output : 12
        Reason: Output is 12 since 12 has value of 200 which is greater than other values
        :param orgDict: Original list passed by the User
        :return: Max value of key  ONLY
        Example : 
        testDict={1:4,10:100,3:90,4:40,6:80,12:200}
        result=func_exec(testDict)
        print(result)
        Expected Output : 12
solution steps:
1. Itertate original dictionary = {1:4,10:100,3:90,4:40,6:80,12:200}
2. from the dictionary to find which key have maximum 
3. finally return the inside dictionary maximum value of key only 
'''

# This function is define maximum value and return the key
def funDict(orgDict):
    #stores list of values from dictionary 
    value=orgDict.values()  
    #items method gives list of tuples from dictionary and key and values iterates Simanatanously
    for _key,_value in orgDict.items():
           #checking for largest value in the dictionary, if condition true it returns the key for that large value
           if (max(value)==_value):
              #finally returns the key of large value pair      
              return _key    
# Execution
testDict={1:4,10:100,3:90,4:40,6:80,12:200}
result=funDict(orgDict=testDict)
print("Final Result is :: {} ".format(result))
