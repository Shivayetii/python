'''Define a dictionary with 10 keys. Multiply each key by 10, each value by 5. 
   Finally iterate and Print the new dict
   :param orgList: to define dictionary and store  10 keys with 10 values into the dictionary by User
   :return: return new dictionary
solution steps:
1. Itertate original dictionary = {20:1,9:2,8:3,30:4,6:5,5:6,40:7,3:8,2:9,50:10}
2. Multiply each key by 10, each value by 5.
3. finally return new dictionary
'''
#  to store 10 keys with 10 values into the dictionary into the original dictionary
org_Dict={20:1,9:2,8:3,30:4,6:5,5:6,40:7,3:8,2:9,50:10}
# define empty dictionary
new_Dict={}
# iterate original dictionary
for key,value in org_Dict.items():
        # each key multiply by 10 and each value multiply by 5 and new keys and values to the new dictionary
        new_Dict[key*10]=value*5
# iterate new dictionary 
for key, values in new_Dict.items():
  # to print the keys and values parallel of the new dictionary
  print(key,value)
# finally return or print the new dictionary
print(new_Dict)