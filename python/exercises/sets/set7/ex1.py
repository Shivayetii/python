'''1. Write a function to take a list. Filter all the even numbers from the ODD indexes. Remove duplicates.
   Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        result=func_exec(listA)
        print(result)
        Expected Output : [20,40,60]
        Example :
        listA=[10,21,30,41,50,50,100,11,12,13]
        result=func_exec(listA)
        print(result)
        Expected Output : [50]
       :param listA: List passed by the User
       :return: Even Elements from ODD indexes without
       duplicates
Solution Steps :
----------------
1. From the list, filter all elements from the ODD index and save it in listODDIndexes array.
2. Iterate listODDIndexes array and filter all even elements and append to new array listEven.
3. Remove duplicates from array listEven.
4. Return listEven.
'''
# this function  filter all elements from the ODD index remove duplicates from array listEven
def funList(orgList):
  # define empty list
  new_lst=[]
  #  Iterate the original lists and filter the values
  for i in range(1,len(orgList),2):
    # this condition it will filter odd indexes so it will give output even elements only
    if (orgList[i]%2==0):
      # add new elements to list
      new_lst.append(orgList[i])
  # finally return new list
  return new_lst
#Execution
#calling function
#Testcase 1
result=funList([10,20,30,40,50,60,100,11,12,13,70])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList([10,20,30,31,41,50])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList([10,30,50,60.70,80])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList([10,20,30,40,50,60,100,1,3,5])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funList([10,20,30,40,50,60,100,11,12,13,50,14,50])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funList([10,20,30,40,50,60,100,11,12,13,111,122,100,101,100])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funList([10,20,30,40,50,60,100,11,12,13,40,30,40,1,40])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funList([10,20,30,40,50,60,100,80,90])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funList([10,20,30,40,50,60,100,11,12,13,30,3,30])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funList([10,20,30,40,50,60,100,11,12,13,10,10])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#