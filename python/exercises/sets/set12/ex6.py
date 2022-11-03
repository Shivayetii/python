'''
6. Write a function to take a dict as argument. Sort the dict by keys and return the dict.
	Example : 
			testDict={1:4,10:20,3:4,4:7,60:11,12:9}
			result=func_exec(testDict)
			print(result)
			Expected Output : {1:4,3:4,4:7,12:9,20:3,60:11}
'''
# Iterate the original dict
def FunDict(org_dict):
    # define new dic
    new_dict={}
    # iterate and sort original dict dict
    for k in sorted(org_dict):
        # Update new dic
        new_dict[k]=org_dict[k]
    # Finally return new dict    
    return new_dict

# Function calling
print(FunDict({1:4,10:20,3:4,4:7,60:11,12:9}))