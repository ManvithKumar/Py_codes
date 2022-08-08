import time

def quick_sort(arr):
    length=len(arr)
    if length<=1:
        return arr
    else:
        pivot=arr.pop()
    
    greater_list=[]
    lesser_list=[]

    for i in arr:
        if i>pivot:
            greater_list.append(i)
        else:
            lesser_list.append(i)
    
    return quick_sort(lesser_list) + [pivot] + quick_sort(greater_list)



arr=[8,6,4,23,1,10,1,0]
start=time.time()
print(start)
print(quick_sort(arr))
end=time.time()
print(end)

    