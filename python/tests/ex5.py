'''Write a function to calculate the student's grade based on marks obtained in various subjects.
   There are 4 subjects Maths, Physics, Chemistry, CSE
   You need to find the sum of all of the marks obtained above and calcuate grade.
   Here's the table to calculcate the grade
   Note: 
       1. You must use **kwargs
       2. If the input score is >100 for any subject you must raise exception since max allowed score is 100 ONLY
       3. If the input score is non-integer, you must raise exception since scores can be in integers ONLY
   ----------------------------
   ----------------------------
       Total       Grade
       ------      ------
        400         A+
        350-400     A
        300-350     B+
        250-300     B
        200-250     C
        150-200     E
        <150        F
'''
def check_grade(**sub_marks):
    sum=0
    for marks in sub_marks.values():
        if (type(marks)==str):
            return("scores can be in integers ONLY")  
        elif(marks>100):
            return(" max allowed score is 100 ONLY")    
        sum=sum+marks    
    if(sum==400):
        return("A+")
    elif(sum>=350 and sum<400):
        return("A")
    elif(sum>=300 and sum<350):
        return("B+")
    elif(sum>=200 and sum<250):
        return("C")
    elif(sum>=150 and sum<200):
        return("E")
    else:
      return("F")
result=check_grade(maths=10,physics=10,chemistry=10,cse=10)
print(result)  