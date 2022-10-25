# While Loop :
# while loop provides to repeat one or more statements while a particular condition is True.
# While loop, the condition is tested before any of the statements in the statement block is executed
# If the condition is True, only then the statements will be executed 
# otherwise if the condition is False, it is jump to next statement which is outside of the while loop.
# Note: If the condition of a while loop is never updated and condition never become False, 
# then the computer will run into an infinite loop.

# Q1
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Q2
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  # Q3
  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

