'''Write a function to take a list, number X as arguments. 
   From the list pick the elements that are not divisible by number X. 
   Add those elements to new list. Finally return the new list.
   :param orgList: Original list passed by the User
   :param numX: Number X passed by the User. Type is INT.
   :return: return new list which elements are not divisible by numX
solution steps:
1. Itertate original list = [1,3,5,7,9,10]
2. from the list filter which elements that are not divisible by numX
3. finally return new list
'''
def fun_List(orgList,numX):
  new_List = []
  for i in orgList:
    if(i%numX!=0):
        new_List.append(i)
  return new_List
# execution
testList=[1,3,5,7,9,10]
numX=2
result=fun_List(orgList=testList,numX=numX)
print("Final Result is :: {} ".format(result))

