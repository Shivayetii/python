def funList(orglistA,orglistB,numx,numy):    
        '''
            1.Write a function to take 2 lists and integers numX,numY .
            From the listA find all elements that are >er sum(numX+numY). Append those elements to listB.
            Remove all duplicates from listB.
            Finally sort and return listB.
            Example :
                listA=[100,20,300,40,50,60,100]
                listB=[1100,20,1300,40,50,160,1000]
                numX=100
                numY=10
                result=func_exec(listA,listB)
                print(result)
                Expected Output : [20,40,50,160,300,1000,1100,1300]
            Example :
                listA=[100,20,300,40,50,60,100]
                listB=[1100,20,1300,40,50,160,1000]
                numX=10
                numY=10
                result=func_exec(listA,listB)
                print(result)
                Expected Output : [20,40,50,60,100,160,300,1100,1300]
            Example :
                listA=[100,20,300,40,50,60,100]
                listB=[1100,20,1300,40,50,160,1000]
                numX=300
                numY=100
                result=func_exec(listA,listB)
                print(result)
                Expected Output : []

            :param org_lists: Original lists (ListA,ListB) passed by the User
            :param numx: Numberx passed by the User. Type is INT.
            :param numy: Numberx passed by the User. Type is INT.

        :return:
            Given:
            listA=[100,20,300,40,50,60,100]
                    listB=[1100,20,1300,40,50,160,1000]
                    numX=100
                    numY=10		
		Expected Output : [20,40,50,160,300,1000,1100,1300]
        Solution Steps:
        **************
        Iterate the original listA
        Check If  condition the sum of original listA elements  is greater than sum of numX+numY
        Append those elements to original list2 
        Remove duplicate from list2 
        Finally return the original list2
        '''

       # Iterate the list
        for ele in orglistA:
            # check listA all elements that are >er sum(numX+numY)
            if (ele>(numx+numy)) and ele not in orglistB:
             # add elements to the listB
                orglistB.append(ele)          
        # Finally return listB
        return sorted(orglistB)
print(funList([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],100,10))  
print(funList([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],10,10))
print(funList([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],300,100))              
