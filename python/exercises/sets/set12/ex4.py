'''
        4.Write a function to take a number numX, numY followed by any number of integer arguments.
            You need to find all numbers divisible by numX and numY
            Filter all the numbers from the list that are divisible numX and numY and add to new list.
            Finally return the new list.
            Note: You must use *args in your function implementation
            *********************************************************
            Example :
                numX=20
                numY=10
                result=func_exec(numX,20,40,50,60,80,90,100,70)
                print(result)
                Expected Output : [20,40,60,80,100]
            Example :
                numX=25
                numY=5        
                result=func_exec(numX,50,60,80,90,100,70)
                print(result)
                Expected Output : [50,100]
            Example :
                numX=7
                numY=12        
                result=func_exec(numX,20,40,50,70)
                print(result)
                Expected Output : []
        :param numbers:*numbers passed by the User
        :param numx: Numberx passed by the User. Type is INT.
        :param numy: Numberx passed by the User. Type is INT.
        :return:
            Given:
            numX=20
            numY=10
            result=func_exec(numX,20,40,50,60,80,90,100,70)	
		Expected Output : [20,40,60,80,100]
        Solution Steps:
        **************
        Iterate the numbers
        Check If  condition the arg numbers are divisible by numX and numy
        Append those elements to newlist
        Finally return the newlist

    Definition of *args:
    when ever we don't know how many positional arguments passed to the function this args are collected the all
    posititional argumentswhile calling the that is called as *args
'''
# Define function
def funKeyArgs(numx,numy,*numbers):
    # Define new list
    new_list=[]
    # Iterate the numbers 
    for ele in numbers:
        # Check numbers are divisible by numx and numy
        if (ele%numx==0 and ele%numy==0):
            # Add to new list
            new_list.append(ele)
    # Finally return new listS        
    return new_list

print(funKeyArgs(20,10,20,40,50,60,80,90,100,70))       
print(funKeyArgs(25,5,50,60,80,90,100,70))
print(funKeyArgs(7,12,50,60,80,90,100,70))     
