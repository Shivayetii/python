'''Write a function to take a dict as an argument. 
	Find the key that has least value and return the key.

	Example : 
		testDict={1:4,10:100,3:90,4:40,6:80,12:200}
		result=func_exec(testDict)
		print(result)
		Expected Output : 1
		Reason: Output is 1 since 1 has value of 4 which is lesser than other values


	Example : 
		testDict={1:4,10:100,3:90,4:40,6:80,12:200,1000:3}
		result=func_exec(testDict)
		print(result)
		Expected Output : 1
		Reason: Output is 1000 since 1000 has value of 3 which is lesser than other values
'''

# This function is define minimum value and return the key
def funDict(orgDict):
    #stores list of values from dictionary 
    val=orgDict.values()  
    #items method gives list of tuples from dictionary and key and values iterates Simanatanously
    for _key,_value in orgDict.items():
           #checking for largest value in the dictionary, if condition true it returns the key for that large value
           if (min(val)==_value):
              #finally returns the key of least value pair      
              return _key    
# Execution
#calling function
#Testcase 1
result=funDict({1:4,10:100,3:90,4:40,6:80,12:200})
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funDict({1:4,10:100,3:90,4:40,6:80,12:200,1000:3})
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funDict({32:3,42:5,75:3,83:13,63:75,61:23})
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funDict({3:2,40:10,45:31,72:73,52:31,55:30})
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funDict({3:5,4:3,5:8,9:5,9:2,12:17})
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=funDict({42:21,57:31,75:31,73:36,83:31,9:12})
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=funDict({12:21,16:61,14:41,17:34,13:31,68:51})
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=funDict({21:42,6:7,4:5,7:8,5:6,3:4})
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=funDict({9:5,8:4,7:3,6:2,5:1,10:7})
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=funDict({180:810,17:71,19:91,270:720,22:22,32:23})
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")