# Sorting by keys:
# Arranging Ascending order of keys

dic={3:5,7:9,2:5,1:2,3:9,4:6}
# Define new dict
new_dic={}
# Sorted keys are assign to _keys variable
keys=sorted(dic.keys())
# Iterate the keys
for i in keys:
    # Update new dictionary
    new_dic[i]=dic[i]
# print new dict    
print(new_dic)
    

