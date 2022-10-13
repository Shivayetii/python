'''Write a function to take a dict, number X and number Y as arguments. 
Multiply each key by number X, each value by number Y. Finally iterate and return the new dict.'''
def dict_multiple(dict_d,x,y):
  output = {}
  for key , value in dict_d.items():
    output[key*x] = value*y
  for key, value in output.items():
    print(key,value)
  return output
print(dict_multiple({1:1,2:2,3:3,4:4,5:5},2,3))