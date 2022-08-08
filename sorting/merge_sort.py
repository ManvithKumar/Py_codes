def merge_sort(arr):
    if len(arr)<=1:
        return 0
    else:
        left_list=arr[:len(arr)//2]
        right_list=arr[len(arr)//2:]

    merge_sort(left_list)
    merge_sort(right_list)

    i=j=k=0
    while i < len(left_list) and j<len(right_list):
        if left_list[i] < right_list[j]:
            arr[k]=left_list[i]
            i+=1
        else:
            arr[k]=right_list[j]
            j+=1
        k+=1
    
    while i < len(left_list):
        arr[k]=left_list[i]
        i+=1
        k+=1
    
    while j < len(right_list):
        arr[k]=right_list[j]
        j+=1
        k+=1
    


arr=[9,8,7,6,5,4,3,2,1]
merge_sort(arr)
print(arr)