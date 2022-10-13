'''Write a function to take a list as an argument. From the list pick the elements that are not divisible by 5.
 Add those elements to new list. Finally return the new list.
'''
def function_list(l1):
  l1 = list(l1)
  l2 = []
  for i in l1:
    if(i%5!=0):
        l2.append(i)
  return l2
print(function_list([1,3,4,10,5,25]))