'''2. Write a function to take a dict, number X,Y as arguments. 
      If the SUM of (dict key + dict val) is PRIME and > sum of number (X+Y)
      then add it to new dict. 
      Finally iterate and return the new dict.
      Example : 
			testDict={1:4,10:2,3:4,4:7,6:11,12:9}
			numX=2
			numY=10
			result=func_exec(testDict,numX,numY)
			print(result)
			Expected Output : {6:11}}

	Example : 
			testDict={1:4,10:2,3:4,4:7,6:11,12:9}
			numX=2
			numY=4
			result=func_exec(testDict,numX,numY)
			print(result)
			Expected Output : {3:4,6:11}}
    :param org_dic: Original dict passed by the User
    :param numx: Numberx passed by the User. Type is INT.
    :param numy: Numbery passed by the User. Type is INT.
    :return: return dictionary with filtered values ONLY.

Solution Steps:
*************
Iterate the dictionary with key and values
Add the dict key and value (key+value)
Check If (key+value) is prime number
Check If prime is > sum of (numberX+numberY) 
If yes:
 Add to new dictionary
     else:
       continue the loop
 Finally return the new dictionary 

'''
#define Function 
def funDict(Org_dict,numX,numY):
  #define new dict
  new_dict={}
  #iterates both key and value from the original dict 
  for key,value in Org_dict.items():
    #storing sum  of present key and value
    sum=key+value  
    #loop for cofactors  
    for cofactor in range(2,sum):
        #checking for prime cofactor divisibility
      if(sum%cofactor==0):
        break
    else:
        #checking for the sum of present key and value is greater than Number X and Number Y
      if(sum>numX+numY):
          #add to new dict
        new_dict[key]=value
  #finally return new dict      
  return new_dict      
#calling function
#Testcase 1
result=funDict({1:4,10:2,3:4,4:7,6:11,12:9},2,10)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funDict({1:4,10:2,3:4,4:7,6:11,12:9},2,4)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funDict({2:3,2:5,7:3,3:8,6:7,6:2},5,8)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funDict({5:6,1:1,4:3,7:30,2:5,5:1},1,2)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funDict({4:3,5:8,9:5,9:2,12:17},2,1)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=funDict({4:20,5:3,7:10,8:8,9:5},3,4)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=funDict({2:11,6:15,14:41,17:19,14:9,15:51},6,5)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=funDict({2:3,6:7,4:5,7:8,5:6,3:4},7,8)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=funDict({8:50,9:4,7:3,6:2,5:17,10:7},7,8)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=funDict({10:200,30:40,2:100,3:10,9:20},10,5)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#