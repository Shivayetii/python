'''3.Write a function to take 2 lists. 
   Use zip function to iterate the list and pick values that
   are common at both indexes
   :param orgDict: Original list passed by the User.
   :return: Iterate the list and pick values that
   are common at both indexes
   Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        result=func_exec(listA,listB)
        print(result)
        # 20 -> listA[1] == listB[1]
        # 40 -> listA[3] == listB[3]
        # 50 -> listA[4] == listB[4]
        Expected Output : [20,40,50]
Solution Steps:
**************
Define the function 
  To define  empty list 
  Iterate the both original lists by using zip 
  Check the comman elements in both lists list 
  Comman elements are add to the empty list 
  Finally print the new List          
'''
# function gives comman elements in listA and listB
def funList(orgListA,orgListB):
# Define Empty List
  new_List = []
# Iterate orgListA and orgListB
  for i,j in zip(orgListA,orgListB):
    print(i,j)
# Checking condition for common indexesvalues of orgListA and orgListB and add new
#  elements to new_list and iteration.
    if (i==j):
      # add elements to new list
      new_List.append(i)
      print(i,j)
# finally returns a new list
  return new_List
#Execution
#calling function
#Testcase 1
result=funList([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList([100,60,50,40,30,20,10,78,80],[1100,20,1300,40,50,160,1000])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList([100,60,50,40,30,20,10,90],[100,20,300,40,50,60,100])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList([100,60,50,30,20,10,110,120],[100,60,50,30,20,10,90])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funList([100,40,30,20,10,210,310],[100,40,30,20,10,110,120])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funList([60,50,40,30,20,10,420,410],[100,60,50,40,30,20,10,110,120])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funList([100,60,50,40,30,510],[100,60,50,40,30,420,410])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funList([100,610,610],[160,420,410])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funList([100,60,20,10,710,720],[100,60,50,40,30,20,10,610])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funList([60,50,40,30,20,10,810,910],[100,60,420,410])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#


