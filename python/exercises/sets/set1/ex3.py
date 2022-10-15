'''Define a dictionary with 10 keys. 
   If the dict key is > 10, then add it to new dict. 
   Finally iterate and print the new dict.
'''
# to define the orginal dictionary and stored 10 key value pairs to the dictionary
orgDict={45:9,89:94,60:78,70:54,54:9,89:4,96:3,73:2,45:8,87:5}
# define empty dictionary
new_Dict={}
# iterate original dictionary
for key,value in orgDict.items():
  # this is checking  condition for which keys are greater than 10 
  if(key>10):
    # new keys and values add to the new dictionary
    new_Dict[key]=value
# iterate the new dictionary 
for keys in new_Dict.keys():
  # to print the  new dictionary keys   
  print(key)
# finally return new dictionary
print(new_Dict)