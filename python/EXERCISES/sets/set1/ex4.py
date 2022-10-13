'''Write a function to take a dict, number X as arguments. 
If the dict key is > number X, then add it to new dict. Finally iterate and return the new dict.'''
def dict_divison(dict_d,x):
  output = {}
  for key, value in dict_d.items():
    if (key>x):
      output[key] = value
  for key, value in output.items():
    print(key,value)
  return output
print(dict_divison( {1:4,3:9,2:6,10:7,19:10,11:12},2))