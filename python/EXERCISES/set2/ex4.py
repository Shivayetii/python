'''Define a list of 10 elements. If the element is even then multiply that element by 100,

if the element is odd then multiply that element by 200. Finally print the new list'''

l1=[11,100,127,99,128,331,990,23,68,10]
l2=[]
for i in l1:
    if(i%2==0):
        l2.append(i*100)
    else:
        l2.append(i*200)
print(l2)