'''
8. Write a function to take a dict as argument. Find the key that has max value.
	Example : 
			testDict={1:4,10:20,3:40,4:7,60:11,12:9}
			result=func_exec(testDict)
			print(result)
			Expected Output : {3:40}
			Reason: Key "3" has value of "40" >er than other values
'''
# Define function
def FunDict(org_dict): 
    new_dict={}
    # Iterate the dic   
    for k,v in org_dict.items():
        # Store the dictionary values in variable
        val=org_dict.values()
        # Find the max value from dictionary
        if (v==max(val)):
            # Update the new dict
            new_dict[k]=v
    # Finally return  the key        
    return new_dict

# Function calling          
print(FunDict({1:4,10:20,3:40,4:7,60:11,12:9}))            
