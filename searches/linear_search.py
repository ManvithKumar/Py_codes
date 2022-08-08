def linear_search(arr,key):
    n=len(arr)
    for i in range(n):
        if arr[i]==key:
            return 1
    
    return 0

li=[1,2,3,4,5,6,7]
key=8
flag=linear_search(li,key)
if flag==1:
    print("Element Found")
else:
    print("Element not Found")

