
'''
    5. Write a function to take 2 lists. Use zip function to iterate the list and pick values that
    are common at both indexes.
	Example :
		listA=[100,20,300,40,50,60,100]
		listB=[1100,20,1300,40,50,160,1000]
		result=func_exec(listA,listB)
		print(result)
		# 20 -> listA[1] == listB[1]
		# 40 -> listA[3] == listB[3]
		# 50 -> listA[4] == listB[4]
		Expected Output : [20,40,50]
	Example :
		listA=[1001,201,3001,401,501,601,1001]
		listB=[1100,20,1300,40,50,160,1000]
		result=func_exec(listA,listB)
		print(result)
		Expected Output : []
	:param orgList: Original listA passed by the User
    :param orgList: Original listB passed by the User
    :return: New list with filtered values ONLY.
            Given:
              listA=[100,20,300,40,50,60,100]
		      listB=[1100,20,1300,40,50,160,1000]
		    Expected Output : [20,40,50]
	Solution Steps:
	1. Take two lists and iterate both list using zip
	2. From the list pick the comman elelments in both lists
	3. Return the list  
'''
#define a function 
def funList(OrgListA,OrgListB):
    #define new list
    newList=[]
    #iterate both lists simantanously with using zip() function
    for listA,listB in zip(OrgListA,OrgListB):
        #checking for listA element s equals to listB element
        if(listA==listB):
            #add to new list
            newList.append(listA)
    #return new list
    return newList

#calling function
result=funList([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000])
print('Final out : {}'.format(result))

result=funList([1001,201,3001,401,501,601,1001],[1100,20,1300,40,50,160,1000])
print('Final out : {}'.format(result))
