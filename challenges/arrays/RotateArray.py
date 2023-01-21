def Rotate_array(arr,k):
    temp1 =[]
    temp2 =[]
    n=0
    for i in arr:
        if n < k :
            temp1.append(i)
            n=n+1
        else:
            temp2.append(i)
    return temp2+temp1
    


arr = [1,2,3,4,5]
k=4
print(Rotate_array(arr,k))