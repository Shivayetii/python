'''4. Write a function to take 2 lists and an integer X. 
	From the listA find all elements that are >er numX. Append those elements to listB.
	Remove all duplicates from listB.
	Finally return listB.
   -------------------------------------------------------------------------------------

	Example :
		listA=[100,20,300,40,50,60,100]
		listB=[1100,20,1300,40,50,160,1000]
		numX=100
		result=func_exec(listA,listB)
		print(result)
		Expected Output : [1100,20,1300,40,50,160,1000,300]

	Example :
		listA=[100,20,300,40,50,60,100,200]
		listB=[1100,20,1300,40,50,160,1000]
		numX=150
		result=func_exec(listA,listB)
		print(result)
		Expected Output : [1100,20,1300,40,50,160,1000,200,300]


	Example :
		listA=[100,20,300,40,50,60,100,200]
		listB=[1100,20,1300,40,50,160,250]
		numX=250
		result=func_exec(listA,listB)
		print(result)
		Expected Output : [1100,20,1300,40,50,160,250]

        :param org_lists: Original lists (ListA,ListB) passed by the User
        :param numx: Numberx passed by the User. Type is INT.
        :return: return list2 with filtered values ONLY.  

Solution Steps:
**************
Iterate the original list1
    Check If the original list number is greater than numberx
    Append those elements to original list2 
    Remove duplicate from list2 
    Finally return the original list2
'''
# Define the function
def funList(orgListA,orgListB,numX):
    # Iterate the original list1
    for i in orgListA:
        # check number is greater numx presence in original list1
        if (i>numX):
            # remove the duplicate in original listB
            if ( i not in orgListB):
                # Original list1 element add to the original list2
                orgListB.append(i)                   
    # Finally return the original list2                
    return orgListB
# Execution
#calling function
#Testcase 1
result=funList([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],100)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=funList([100,20,300,40,50,60,100,200],[1100,20,1300,40,50,160,1000],150)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=funList([100,20,300,40,50,60,100,200],[1100,20,1300,40,50,160,250],250)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=funList([1,10,8,7,4,3,6,2,9,5],[32,12,8,23,27,3,62,32,21,5],5)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=funList([1000,800,300,500,700,100,600,400,900],[77,42,67,500,787,100,672,48,900],100)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=funList([21,34,57,87,54,32,23,29,55,80],[21,13,72,87,54,43,78,90,55,88],500)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=funList([90,100,98,93,95,91,96,92,97,99],[76,42,67,66,34,59,42,57,63,48],4)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=funList([1,100,300,800,50,39,75,67,894],[1,88,76,82,35,39,75,79,86],5)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=funList([25,45,65,75,95,105,25,15,85],[14,35,75,88,95,78,25,71,85],3)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=funList([121,22,456,2337,980,432,666,77,9],[34,75,78,64,980,463,777,72,48],143)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
