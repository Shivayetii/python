'''
		Write a function to take a list argument. Find the element that has greatest length.
			Example :
				listA=["hello","world","science","maths","Python"]
				result=func_exec(listA)
				print(result)
				Expected Output : ["science"]
				Reason: length of science -> 7
			Example :
				listA=["hello","world","science","maths","Pythonics"]
				result=func_exec(listA)
				print(result)
				Expected Output : ["Pythonics"]
				Reason: length of Pythonics -> 9

			:param org_list: Original list passed by the User
			:return:
            :Given:
               listA=["hello","world","science","maths","Python"]
			:Expected Output : ["science"]

			Solution Steps:  
			**************
			    Take original list and iterate
				Store sizes of words in a list 
				checking if the word size is greater than remaining words
				if yes:
					add to new list
				else:
					continue loop
			    Finally return the greater length lenth of list					
'''
# Define function
def funList(org_list):
	# Maximun length is start from 0 
    max_len=0
	# Iterate the original list
    for ele in org_list:
		# Check condition for length of the list is greater than 0
        if (len(ele)>max_len):
			# max length of element from the list
            max_len=len(ele)
			# result is Assign to variable 
            gre_len=ele
	# Finally return the greatest length word from list			
    return gre_len                    
#calling function  
result=funList(["hello","world","science","maths","Python"])
print('Result : {}'.format(result))

result=funList(["hello","world","science","maths","Pythonics"])
print('Result : {}'.format(result))