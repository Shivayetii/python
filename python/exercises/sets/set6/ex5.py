'''5. Write a function to take a dict and number X as argument. 
      Find the key,value pairs that are both divisible by number X
    Example1 : 
            testDict={10:20, 3:30, 4:40,90:100,20:30}
            numX=10
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {10:20,90:100,20:30}
    Example2 : 
            testDict={10:20, 3:30, 4:40,90:100,20:30}
            numX=20
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {}
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
#calling function
#Testcase 1
result=funDict({10:20, 3:30, 4:40,90:100,20:30},10)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funDict({10:20, 3:30, 4:40,90:100,20:30},20)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funDict({10:200, 3:30, 4:16,90:10,20:31,11:23,17:44,20:40},30)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funDict({10:20, 3:30, 4:16,90:100,20:31,11:23,17:44,20:40},5)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funDict({10:20, 3:30, 4:16,90:10,20:31,22:20,17:44,20:40},2)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funDict({10:20, 3:30, 4:16,90:10,20:40,11:230,17:44,20:40},4)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funDict({10:20, 30:300, 4:16,90:90,20:31,11:23,16:48,20:400},6)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funDict({10:20, 30:300, 4:16,90:100,30:600,11:23,17:44,90:900,30:500},30)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funDict({10:20, 3:300, 4:16,90:100,20:31,200:800,17:44,40:400},40)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funDict({10:20, 3:300, 4:16,90:100,20:31,11:23,17:44,20:400,40:600},50)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#