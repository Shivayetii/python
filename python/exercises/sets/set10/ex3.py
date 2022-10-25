'''3. Write a function to take a list argument. Find the element that has greatest length.
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
        :return: New list with filtered values ONLY.  

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
    for i in org_list:
		# Check condition for length of the list is greater than 0
        if (len(i)>max_len):
			# max length of element from the list
            max_len=len(i)
			# result is Assign to variable 
            gre_len=i
	# Finally retyrn the greatest length word from list			
    return gre_len        
            
#calling function  
# Execution
#calling function
#Testcase 1
result=funList(["hello","world","science","maths","Python"])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList(["hello","world","science","maths","Pythonics"])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList(["hello","world","today"])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList(["hello","world","today","python"])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funList(["hello","world","today","yesterday","exercisesexamples",""])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 6
result=funList(["hello","sets","quires"])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 7
result=funList(["hello","sets","quires","assignments"])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 8
result=funList(["dictionaries","sets","quires","assignments"])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 9
result=funList(["functions","sets","quires"])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 10
result=funList(["functions with arguments","sets","quires"])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#

