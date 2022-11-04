'''
8. Write a function to take a dict as argument. Find the key that has max value.
	Example : 
			testDict={1:4,10:20,3:40,4:7,60:11,12:9}
			result=func_exec(testDict)
			print(result)
			Expected Output : {3:40}
			Reason: Key "3" has value of "40" >er than other values
    :param orgDict: Original list passed by the User
    :return: Max value of key  ONLY and return newDict
    Given:
              testDict={1:4,10:20,3:40,4:7,60:11,12:9}
		      Expected Output : {3:40}
    olution Steps:
        **************
        Define the  function 
        To define one empty dictionary
        To store the values in original dictionary
        Iterate the original dictionary = {1:4,10:20,3:40,4:7,60:11,12:9}
        to check the maximum key value in dictionary
        Finally print the new dictionary   
'''
# Define function
def funDict(org_dict): 
    new_dic={}
    # Iterate the dic   
    for key,value in org_dict.items():
        # Store the dictionary values in variable
        val=org_dict.values()
        # Find the max value from dictionary
        if (value==max(val)):
            # Update the new dict
            new_dic[key]=value
    # Finally return  the key        
    return new_dic

# Function calling          
print(funDict({1:4,10:20,3:40,4:7,60:11,12:9}))   