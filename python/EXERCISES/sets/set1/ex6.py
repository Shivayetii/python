'''Write a function to take a list, number X, number Y as arguments. 
   If the element is even then multiply that element by number X.
   if the element is odd then multiply that element by number Y.
   Finally return the new list.
   :param orgList: Original list passed by the User
   :param numX: Number X passed by the User. Type is INT.
   :param numX: Number X passed by the User. Type is INT.
   :return: return new list
solution steps:
1. Itertate List original list = [1,3,5,7,9,10]
2. and then check the conditions If the element is even then multiply that element by numX
3. if the element is odd then multiply that element by numY
4. finally return new list
'''
# this function will define even elements are multiply by numX and odd elements are multiply numY
def fun_List(orgList,numX,numY):
   # define empty list
  new_List = []
  # iterate original list
  for i in orgList:
    # check if condition it true so even elements multiply by numX 
    # it is not true then it will goes to else condition
    if(i%2==0):
        # which elements multiply by numX those elements are add to the new list
        new_List.append(i*numX)
    # odd elements are multiply by numY
    else:
        # which elements are multiply by the numY those elements are add to the new list
        new_List.append(i*numY)
  # finally return new list
  return new_List
# execution
testList=[1,3,5,7,9,10]
numX=2
numY=3
result=fun_List(orgList=testList,numX=numX,numY=numY)
print("Final Result is :: {} ".format(result))