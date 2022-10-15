'''Write a function to take a list as an argument. 
   If the element is even then multiply that element by 100.
   if the element is odd then multiply that element by 200. 
   Finally return the new list.
   :param orgList: Original list passed by the User
   :param numX: Number X passed by the User. Type is INT.
   :return: return new list
solution steps:
1. Itertate List original list = [1,3,5,7,9,10]
2. and then check the conditions If the element is even then multiply that element by 100.
3. if the element is odd then multiply that element by 200.
4. finally return new list
'''
# this function will define even elements are multiply by 100 and odd elements are multiply 200
def fun_List(OrgList):
  # define empty list
  new_List = []
  # iterate original list
  for x in OrgList:
    # check if condition it true so even elements multiply by 100 
    # it is not true then it will goes to else condition
    if(x%2==0):
      # which elements multiply 100 those elements are add to the list
      new_List.append(x*100)
    # odd elements are multiply by 200 
    else:
      # which elements are multiply by the 200 those elements are add to the new list
      new_List.append(x*200)
  # finally return new list
  return new_List
# Execution
testList=[1,3,5,7,9,10]
result=fun_List(OrgList=testList)
print("Final Result is :: {} ".format(result))
