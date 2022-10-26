# Sorting by values:
# Arranging Ascending order of values

dic={10:5,20:10,2:3,4:6}
# Define new dict
new_dic={}
# Sorted keys are assign to _keys variable
val=sorted(dic.values())

#iterates values one by one
for keys in val:
    #iterates keys from original dict one by one
    for _val in dic:
        #checking for values and keys if condition true it adds to new dict.
        if(keys==dic[val]):
            #add key-value pair to new dictionary
            new_dic[val]=keys
# Print new_dict            
print(new_dic)            