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
testList=[10,20,30,40,50,60,100,11]
#function calling
result=funList(org_list=testList)
#finally print result
print("Final Result is :: {} ".format(result))    

def check_lst(lst):
  new_lst=[]
  for i in range(1,len(lst),2):
    if (lst[i]%2==0):
      new_lst.append(lst[i])
  return new_lst
print(check_lst([10,21,30,41,50,50,100,11,12,13]))