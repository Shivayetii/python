# Update Dictionary
# Inserts the specified items to the dictionary.

#Q1
dic={2:3,6:7,4:5,7:8,5:6,3:4}
dic.update({10:20})
print(dic)
a={1:10,2:20,3:30}
a[100]=200
print(a)

#Q2
dic={2:3,6:7,4:5,7:8,5:6,3:4}
dic.update({10:20,100:200})
print(dic)
a={1:10,2:20,3:30}
a[100]=200
a[100]=1000
print(a)
