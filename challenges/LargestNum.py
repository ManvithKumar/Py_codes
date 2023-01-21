def LargestNum(str):
    nlist=[]
    n_str=""
    for i in str:
        nlist.append(i)
    nlist.sort(reverse=True)
    for i in nlist:
        n_str=n_str+i
    return n_str[0] ,n_str[1]

n1,n2 =LargestNum('54321')
print(n1)
print(n2)
