'''Define a dictionary with 10 keys. Multiply each key by 10, each value by 5. 
Finally iterate and Print the new dict'''
d1={20:1,9:2,8:3,30:4,6:5,5:6,40:7,3:8,2:9,50:10}
d2={}
for key,value in d1.items():
        d2[key*10]=value*5
for key in d2.keys():
  print(key)
print(d2)