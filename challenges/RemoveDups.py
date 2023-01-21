def RemoveDups(str):
    l1={}
    for i in str:
        if i not in l1:
            l1[i]=1
        if i in l1:
            continue
    str=""
    for x,y in l1.items():
        str+=x
        
    return str

str = "helllomanvvith"
print(RemoveDups(str))



