# For_Loop :
# The for loop provides to repeat a task until a particular condition is true.
# For loop is known as a determine exactly how many times the loop will repeat.
# The number of times the loop has to be executed can be determined logic of the loop

# Program to find the sum of all numbers stored in a list

#Q1
org_list=[15,20,30,115,120,80,580,310,40,50]
new_list=[]
for i in org_list:
  if(i>100):
    new_list.append(i)
print(new_list) 
#Q2
orgDict={45:9,89:94,60:78,70:54,54:9,89:4,96:3,73:2,45:8,87:5}
# define empty dictionary
new_Dict={}
for key,value in orgDict.items():
  if(key>10):
    new_Dict[key]=value
for keys in new_Dict.keys(): 
  print(key)
print(new_Dict)