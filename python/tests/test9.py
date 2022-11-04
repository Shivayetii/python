def func_exec(**ratings):
	'''
		Note: 
		   	1. You must use **kwargs
		   	2. If the rating score is >100 for any employee you must raise exception since max allowed score is 100 ONLY
		   	3. If the input score is non-integer, you must raise exception since scores can be in integers ONLY
		   	4. Formula for new salary calculation:
		   		new_salary= ((hike/100)*old_salary)+old_salary
		   		Example:
		   			curr_salary=100000
		   			hike=30
		   			new_salary=((30/100)*100000)+100000
		   			new_salary=130000

		   			curr_salary=50000
		   			hike=10
		   			new_salary=((10/100)*50000)+50000
		   			new_salary=55000
		   Here's the table to calculcate the hike
			   Total       Hike%
			   ------      ------
			    100         30
			    90-100      24
			    80-90       17
			    70-80       12
			    60-70       8
			    50-60       4
			    <50         1
			Example :
				result=func_exec(rating=100,curr_salary=100000)
				print(result)
				Expected Output : {"hike":"30","new_salary":"130000"}

			Example :
				result=func_exec(rating=49,curr_salary=100000)
				print(result)
				Expected Output : {"hike":"1","new_salary":"101000"}

			Example :
				result=func_exec(rating=200,curr_salary=50000)
				print(result)
				Expected Output : Raise Exception since rating score is 200, max allowed rating score is 100 ONLY

			Example :
				result=func_exec(rating="100",curr_salary=50000)
				print(result)
				Expected Output : Raise Exception since rating score is a string "100", rating scores can be integers ONLY

    Definition of keywargs:
    when ever we don't know how many key value pairs  passed to the function this keywargs are collected the all
    key-value pairs while calling the function  that is called as **keywargs

	:params
	--------
	:param rating: Rating for the given Employee
	:param curr_salary: Current Salary of the Employee

	:return:
	--------	
		Given the rating, find the hike and new salary and return		
		Expected Output : {"hike":"30","new_salary":"130000"}
        
	:exceptions:
	------------

	Raise exceptions for following cases;
		
		1. Rating is >100
		2. Rating or Current Salary is String
	'''
	# Find the rating and current salary
	rating=ratings['rating']
	curr_salary=ratings['curr_salary']

	# Check and raise exceptions
	if type(rating)==str or type(curr_salary)==str:
		raise ValueError("Rating and Current Salary must be in Int/Float ONLY")
	if rating>100:
		raise ValueError("Max allowed Rating is 100 ONLY")

	# Set default value for hike
	hike=0

	# Run if checks to find HIKE
	# * * * * * * * * * * * * * *

	#Check if rating is 100
	if rating==100:
		hike=30

	#Check if rating is >90 and <100
	elif rating>90 and rating<100:
		hike=24		

	#Check if rating is >80 and <90
	elif rating>80 and rating<90:
		hike=17
	
	#Check if rating is >70 and <80
	elif rating>70 and rating<80:
		hike=12
	
	#Check if rating is >60 and <70
	elif rating>60 and rating<70:
		hike=8
	
	#Check if rating is >50 and <60
	elif rating>50 and rating<60:
		hike=4
	
	# else return lowest hike
	else:
		hike=1

	# Based on the hike, find the new salary
	# new_salary= ((hike/100)*old_salary)+old_salary
	new_salary=((hike/100)*curr_salary)+curr_salary
	return {"hike":hike,"new_salary":new_salary}


#Execution
result=func_exec(rating=100,curr_salary=100000)
print(result)