def fun_dict(org_dict):
    values=org_dict.values()
    for key,value in org_dict.items():
        if(max(values)==value):
            return key
print(fun_dict({1:10,2:20,10:2}))