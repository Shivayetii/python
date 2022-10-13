
'''Define a dictionary with 10 keys. If the dict key is > 10, then add it to new dict.
Finally iterate and print the new dict.'''
d1={20:1,9:2,8:3,30:4,7:5,5:6,4:7,3:8,80:9,70:10}
d2={}
for key,value in d1.items():
    if(key>10):
        d2[key]=value
for key in d2.keys():
  print(key)
print(d2)