'''2. Write a function to take a number numX, numY followed by any number of integer arguments.
    You need to find all numbers divisible by numX and numY
    Filter all the numbers from the list that are divisible numX and numY and add to new list.
    Finally return the new list.
    Note: You must use *args in your function implementation
    *********************************************************
    Example :
        numX=20
        numY=10
        result=func_exec(numX,20,40,50,60,80,90,100,70)
        print(result)
        Expected Output : [20,40,60,80,100]
    Example :
        numX=25
        numY=5        
        result=func_exec(numX,50,60,80,90,100,70)
        print(result)
        Expected Output : [50,100]
    Example :
        numX=7
        numY=12        
        result=func_exec(numX,20,40,50,70)
        print(result)
        Expected Output : []
    :param numX: Number X passed by the User. Type is INT.
    :param numY: Number Y passed by the User. Type is INT.
    :param *args: arguments passed by the User. Type is INT.
    :return: Finally return new list 
Solution Steps:
**************
Define the function  
  To define  empty list and iterate the args
  To check the if condition which arguments are divisible by numX and numY
  To add the which are arguments are  divisible by numX and numY those arguments are  add to the new list
  Finally print the new list
'''
# To define a function for to filter the which args are divisible by numX and numY
def funArgs(numX,numY,*args):
  # To define empty list
  new_List = []
  # To iterate the which numbers are passed in args
  for i in args:
    # this is checking the condition for which numbers are divisible by numX and numY
    # if condition is true it will execute if statment
    if (i%numX==0 and i%numY==0):
      # to add the which are numbers divisible by numX  and numY those numbers add to the new list 
      new_List.append(i)
  # finally return new list
  return new_List
#Execution
#calling function
#Testcase 1
result=funArgs(20,10,20,40,50,60,80,90,100,70)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funArgs(25,5,50,60,80,90,100,70)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funArgs(7,12,20,40,50,70)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funArgs(8,10,60,80,90,100,70)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funArgs(6,4,40,50,60,80,90,100,70)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funArgs(15,8,40,50,60,80,90,100,70)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funArgs(6,2,40,50,60,80,90,100,70)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funArgs(3,4,40,50,60,80,90,100,70)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# Testcase 9
result=funArgs(5,10,40,50,60,80,90,100,70,200,210,300)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# Testcase 10
result=funArgs(8,9,40,50,60,80,90,100,70,200,210,300)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#