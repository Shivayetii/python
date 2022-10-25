# if-elif-else Statement: 
# if statments is always contains the true values or true conditions only
# else also will be contains  true values or true conditions only
# If and elif both conditions are failled loop will go to the else block 
# else block always contains false conditions only

#Q1
a=200
b=100
# if condition is true so executed if statment
if a > b:
    print("a is greater than b")
# elif condition is not true so the loop is stop above the if statment because if statement is true
# so it will print if statment condition only
elif a < b:
    print("a is less than b")
# above the if condition is true so the not comes to else statment
else:
    print("a is equal to b")

#Q2
a=200
b=100
#Q3
a=200
b=100
# if condition is not  true so the loop will goes to elif statment
if a < b:
    print("a is greater than b")
# elif  condition is true so it will executed elif statment only
elif a > b:
    print("a is greater than b")
# above else conditions is true so the doesn't comes else block
else:
    print("a is equal to b")
#Q3
a=200
b=100
#Q3
a=200
b=100
# if condition is not  true so the loop will goes to elif statment
if a < b:
    print("a is greater than b")
# elif  condition is not true so the loop will goes to else block
elif a < b:
    print("a is greater than b")
# above the if and elif conditions are not true the loop will goes to 
# else block then it will execute else block only
else:
    print("a is equal to b")