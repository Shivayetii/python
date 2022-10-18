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

#calling function
#Testcase 1
result=funList([10,20,30,40,50,60,100,11,12,13])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList([10,21,30,41,50,500,100,11,12,13,21])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList([10,21,30,41,50,50,100,11,12,13,21])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList([10,20,30,40,50,60,100,11,12,13,13,14,13])
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
result=funList([10,20,30,40,50,60,100,11,12,13,20,1,20])
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