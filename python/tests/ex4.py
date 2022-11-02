'''Write a function to take a dict as argument. Find the key that has max value.
    Example : 
            testDict={1:4,10:20,3:40,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {3:40}
            Reason: Key "3" has value of "40" >er than other values
'''

def funDict(orgDict):
    i = orgDict.values()
    newDict={}
    for key,value in orgDict.items():
        if(max(i)==value):
            newDict[key]=value
    return newDict
print(funDict({1:4,10:20,3:40,4:7,60:11,12:9,13:400}))