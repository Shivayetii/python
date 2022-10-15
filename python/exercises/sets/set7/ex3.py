'''
3. Write a function to take a list. From the list find the number that occurs most number of times.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        result=func_exec(listA)
        print(result)
        Expected Output : []
    Example :
        listA=[10,21,30,41,50,500,100,11,12,13,21]
        result=func_exec(listA)
        print(result)
        Expected Output : [21,]
    Example :
        listA=[10,21,30,41,50,50,100,11,12,13,21]
        result=func_exec(listA)
        print(result)
        Expected Output : [21,50]
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY.  
Solution Steps:
**************
Iterate the orginal list 
  Check condition for most repeated element in the list and remove the duplicate numbers
      If yes:
        add the new list
      else:
        continue the loop  
Add finally retun the new list
'''
# This function is define most number of times element
def funList(org_list):
  #define new empty list 
  new_list=[]  
  #iterates original list on by one  
  for i in org_list:
    #checking for number not present in new list    
    if(i not in new_list):
      #checking fo number than occurs repeatedly      
      if(org_list.count(i)>1):
        #ads number to new list
        new_list.append(i)
  #finally returns new list        
  return new_list
# Execution
testorg_list=[10,20,30,40,50,60,100,11,12,13]
#function calling
result=funList(org_list=testorg_list)
#finally print result
print("Final Result is :: {} ".format(result)) 