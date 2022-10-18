'''2.Write a function to take a list. Sort and return the new list.
:param orgDict: Original list passed by the User
:return: sorted New list from orgList.
Example :
        listA=[100,20,300,40,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : [20,40,50,60,100,100,300]
Solution Steps:
**************
Define the function  
  To define  empty list Iterate the original list 
  Sorted the Ogiginal list = [100,20,300,40,50,60,100]
  Sorted list elements is  add to the empty list 
  Print the new list
'''
# define function for sorted the list
def funList(orgList):
  # Define Empty list
  newMapper = []
  # sort the orginal list
  for i in sorted(orgList):
    # add the elements in new list
    newMapper.append(i)
  #Finally return new sorted list 
  return newMapper
#Execution
#calling function
#Testcase 1
result=funList([100,60,50,40,30,20,10])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList([100,60,50,40,30,20,10,78,80])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList([100,60,50,40,30,20,10,90])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList([100,60,50,40,30,20,10,110,120])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funList([100,60,50,40,30,20,10,210,310])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funList([100,60,50,40,30,20,10,420,410])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funList([100,60,50,40,30,20,10,510])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funList([100,60,50,40,30,20,10,610])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funList([100,60,50,40,30,20,10,710,720])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funList([100,60,50,40,30,20,10,810,910])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#


