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
        Expected Output : [20,40,50]'''
# function gives comman elements in listA and listB
def fun_List(orgListA,orgListB):
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
# Execution
testListA=[100,20,300,40,50,60,100]
testListB=[1100,20,1300,40,50,160,1000]
result=fun_List(orgListA=testListA,orgListB=testListB)
print("Final Result is :: {} ".format(result))