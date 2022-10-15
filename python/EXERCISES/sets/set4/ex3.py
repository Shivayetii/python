'''3.Write a function to take a list as an argument. 
   Find all the elements that occur in EVEN indexes
   :param orgList: Original list passed by the User
   :return: Get out put Eindexes from list ONLY
    Example : 
        listA=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10,300]
        result=func_exec(listA)
        print(result)
        Expected Output : [1,300,5,7,8,19,11,200]
solution steps:
1. Itertate original lister = [1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
2. from the list to filter the even indexes
3. finally return new list
'''
#This function gives new list with even index elements from original list
def funList(orgList):
  #define new empty list
  new_List = []
  #loop i variable contains even numbers and step number is 2
  for index in range(0, len(orgList), 2):
    #even index elements from original list is adds to new list
    new_List.append(orgList[index])
# finally returns a new list of ODD indexes 
  return new_List
# Execution
testList=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
result=funList(orgList=testList)
print("Final Result is :: {} ".format(result))
