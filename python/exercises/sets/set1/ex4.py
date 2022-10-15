'''Define a list of 10 elements. 
   If the element is even then multiply that element by 100, 
   if the element is odd then multiply that element by 200. Finally print the new list.
'''
# Define original list and soter 10 elements to the list
org_list=[15,20,30,115,120,80,580,310,40,50]
# Define new list
new_list=[]
# Iterate the original 
for i in org_list:
  # this is checking the condition for if the elements are even so the element is multiple by 100 it is not true
  # then goes to else statment
  if(i % 2 == 0):
    # new even elements add to the list
    new_list.append(i*100)
  # it will filter odd elements in side the list
  else:
    # add odd elements to the list
    new_list.append(i*200)
# finally return new list
print(new_list)    