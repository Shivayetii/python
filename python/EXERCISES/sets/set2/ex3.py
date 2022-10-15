
'''Define a dictionary with 10 keys. If the dict key is > 10, then add it to new dict.
   Finally iterate and print the new dict.
   :param orgList: to define dictionary and store  10 keys with 10 values into the dictionary by User
   :return: return new dictionary
solution steps:
1. Itertate original dictionary = {20:1,9:2,8:3,30:4,7:5,5:6,4:7,3:8,80:9,70:10}
2. from the dictionary filter which keys are greater than 10 those keys are add to the new dictionary
3. finally iterate new dictionary and return or print new dictionary
'''

#  to store 10 keys with 10 values into the dictionary into the original dictionary
org_Dict={20:1,9:2,8:3,30:4,7:5,5:6,4:7,3:8,80:9,70:10}
# define empty dictionary
new_Dict={}
# iterate original dictionary
for key,value in org_Dict.items():
    # this is checking the condition for which keys are greater than 10
    if(key>10):
        # which keys are greater than 10 those elements are add to the new dictionary
        new_Dict[key]=value
# iterate new dictionary
for key, value in new_Dict.items():
  # to print the keys and values parallel of the new dictionary
  print(key,value)
# finally return or print the new dictionary
print(new_Dict)