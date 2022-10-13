'''Write a function to take a list, number X, number Y as arguments. 
If the element is even then multiply that element by number X, if the element is odd then multiply that element by number Y.
 Finally return the new list.
'''
def function_list(l1,x,y):
  l1 = list(l1)
  l2 = []
  x = int(x)
  for i in l1:
    if(i%2==0):
        l2.append(i*x)
    else:
        l2.append(i*y)
  return l2
print(function_list([1,2,5,6,9,10],3,4))